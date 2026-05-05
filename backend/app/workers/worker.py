import asyncio
import time
import uuid
from app.services.debounce import get_or_set_debounced_work_item
from app.core.mongo import mongo_db
from app.services.queue import pop_from_queue

async def process_single_signal(signal_data: dict):
    """
    Core logic to process an incoming signal from the Redis queue.
    """
    component_id = signal_data.get('component_id')
    
    # 1. Check Redis for an existing debounced incident
    existing_work_item_id = await get_or_set_debounced_work_item(component_id, "PENDING_CREATION")
    
    if existing_work_item_id:
        # DEBOUNCED: Rate limiting kicked in
        work_item_id = existing_work_item_id
        print(f"Debounced! Linking signal to existing WorkItem: {work_item_id}")
    else:
        # NEW INCIDENT: Generate a new ID (Simulating PostgreSQL Creation)
        work_item_id = str(uuid.uuid4())[:8]
        
        # Update Redis with the 10-second TTL
        await get_or_set_debounced_work_item(component_id, work_item_id)
        print(f"New Incident! Created WorkItem: {work_item_id}")

    # 2. ALWAYS save the raw signal to the MongoDB Data Lake
    raw_document = {
        "work_item_id": work_item_id,
        "payload": signal_data,
        "timestamp": signal_data.get('timestamp')
    }
    await mongo_db.raw_signals.insert_one(raw_document)

async def start_worker():
    print("========================================")
    print("Worker successfully started!")
    print("Connected to MongoDB & Redis Queue.")
    print("Listening for incoming high-volume signals...")
    print("========================================")
    
    signals_processed_in_window = 0
    last_metric_time = time.time()

    # This infinite loop keeps the Docker container alive!
    while True:
        # 1. Pull the next signal from Redis (waits up to 1 second)
        signal_data = await pop_from_queue()
        
        if signal_data:
            # 2. Process the payload
            await process_single_signal(signal_data)
            signals_processed_in_window += 1
            
        # 3. Observability Requirement: Calculate & print metrics every 5 seconds
        current_time = time.time()
        time_elapsed = current_time - last_metric_time
        
        if time_elapsed >= 5.0:
            throughput = signals_processed_in_window / time_elapsed
            print(f"[METRICS] Current Throughput: {throughput:.2f} Signals/sec")
            
            # Reset counters for the next 5-second window
            signals_processed_in_window = 0
            last_metric_time = current_time

# This block is what actually executes the code when the file runs
if __name__ == "__main__":
    asyncio.run(start_worker())

import redis.asyncio as redis
import json

# Connect to the Redis container using the async client
r = redis.from_url("redis://ims-redis:6379", decode_responses=True)
QUEUE_NAME = "signal_queue"

async def enqueue_signal(payload):
    """Pushes a new signal to the queue from the FastAPI API."""
    print("🔥 enqueue_signal CALLED")
    try:
        # rpush adds to the right side of the list
        result = await r.rpush(QUEUE_NAME, json.dumps(payload))
        print(f"✅ Redis RPUSH result: {result}")
    except Exception as e:
        print("❌ REDIS ERROR:", e)

async def pop_from_queue():
    """Pops a signal from the queue for the Worker to process."""
    try:
        # blpop waits for up to 1 second for a signal to arrive
        result = await r.blpop(QUEUE_NAME, timeout=1)
        if result:
            # result is a tuple: (queue_name, data)
            _, data = result
            return json.loads(data)
        return None
    except Exception as e:
        # Fails silently on timeout, which is normal when the queue is empty
        return None

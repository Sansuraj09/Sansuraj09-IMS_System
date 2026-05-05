import redis.asyncio as redis
from typing import Optional

# Using the modern redis.asyncio, and pointing to the Docker service name
redis_client = redis.from_url("redis://ims-redis:6379", decode_responses=True) 

async def get_or_set_debounced_work_item(component_id: str, new_work_item_id: str) -> Optional[str]:
    """
    Checks if a component recently failed. 
    Returns existing WorkItem ID if debounced, otherwise sets new and returns None.
    """
    debounce_key = f"debounce:{component_id}"
    
    existing_id = await redis_client.get(debounce_key)
    
    if existing_id:
        return existing_id
        
    await redis_client.set(debounce_key, new_work_item_id, ex=10)
    return None

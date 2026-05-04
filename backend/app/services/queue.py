import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

async def enqueue_signal(payload):
    r.lpush("signal_queue", json.dumps(payload))

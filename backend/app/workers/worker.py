import redis
import json
import time

r = redis.Redis(host="redis", port=6379, decode_responses=True)

print("Worker started...")

while True:
    data = r.rpop("signal_queue")

    if data:
        signal = json.loads(data)
        print("Processing:", signal)
    else:
        time.sleep(1)

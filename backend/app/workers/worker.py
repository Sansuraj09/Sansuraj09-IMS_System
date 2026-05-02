import redis
import json
import time

r = redis.Redis(host="redis", port=6379)

while True:
    data = r.rpop("signals")

    if data:
        signal = json.loads(data)
        print("Processing:", signal)
    else:
        time.sleep(1)

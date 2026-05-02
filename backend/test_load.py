import requests

for i in range(10000):
    requests.post("http://localhost:8000/signals", json={
        "component_id": "db",
        "severity": "P0"
    })

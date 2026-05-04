import requests
import time
import random


from datetime import datetime, timezone
"timestamp": datetime.now(timezone.utc).isoformat()
API_URL = "http://localhost:8000/ingest"

components = [
    ("RDBMS_PRIMARY", "orders-db", "P0"),
    ("CACHE_CLUSTER_01", "redis-cache", "P2"),
    ("MCP_HOST_02", "mcp-worker", "P1")
]

errors = {
    "RDBMS_PRIMARY": ["Connection timeout", "Deadlock detected", "Query failure"],
    "CACHE_CLUSTER_01": ["Cache miss spike", "Eviction surge"],
    "MCP_HOST_02": ["Worker crash", "Restart failure", "Queue backlog"]
}

def generate_signal(component, service, severity):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "component_id": component,
        "service": service,
        "severity": severity,
        "error": random.choice(errors[component]),
        "latency_ms": random.randint(500, 6000)
    }

def run_simulation():
    print("Starting IMS failure simulation...")

    for _ in range(50):
        for comp, service, severity in components:
            payload = generate_signal(comp, service, severity)

            try:
                requests.post(API_URL, json=payload)
                print(f"Sent: {payload['component_id']} - {payload['error']}")
            except Exception as e:
                print("API Down / Rate limited:", e)

        time.sleep(0.5)

if __name__ == "__main__":
    run_simulation()

# Incident Management System (IMS)

# Overview
This Incident Management System (IMS) is a distributed monitoring engine designed to handle high-volume service signals, process them asynchronously with debouncing logic, and display them in a real-time dashboard. 

It full fills all requirements of the Engineering Challenge, demonstrating:
-> Microservice-style backend design
-> High-throughput signal ingestion via API
-> Queue-based processing and Backpressure handling (Redis)
-> NoSQL Data Lake persistence (MongoDB)
-> Frontend dashboard visualization (React/Vite)
-> State-machine guardrails (Mandatory RCA)

# System Architecture Diagram

        +-------------------+
        |   React Frontend  |
        | (Vite Dashboard)  |
        +-------------------+
                 | (REST API Polling)
        +-------------------+
        |   FastAPI API     |
        |  /signals endpoint|
        +--------+----------+
                 | (RPUSH)
        +-------------------+
        |      Redis        |
        | (Queue Buffer)    |
        +-------------------+
                 | (BLPOP)
                 v
        +-------------------+
        | Background Worker |
        | (Async Processor) |
        +-------------------+
                 | (Insert/Update)
                 v
        +-------------------+
        |     MongoDB       |
        | (NoSQL Data Lake) |
        +-------------------+

 The Tech StackFrontend: React (Vite)Backend: FastAPI (Python)Queue/Buffer: RedisWorker: Python Background Consumer (Asyncio)Database: MongoDBOrchestration: Docker + Docker Compose.
 Quick StartGet the entire system up and running in under two minutes.
 1. Clone & EnterBashgit clone <your-repository-url>
  cd incident-management-system

3. Launch ContainersThis spins up the Frontend (Port 5173), Backend (Port 8000), Redis, and MongoDB.
   
   insrtall docker + docker compose
   "docker compose up -d --build"
    "docker ps"
   
4. Monitor the WorkerTo see throughput metrics and real-time signal processing in the terminal:                              docker logs -f ims-worker
   
5. Testing the System (The Simulator)To simulate a "High-Volume Failure Event" (like a major RDBMS outage), run the included Python script in a new terminal window
   "python3 scripts/simulate_signals.py"
   
What to watch for:The Worker Logs: You’ll see the worker debouncing duplicate signals and reporting Signals/sec metrics.
 The Dashboard: Open http://localhost:5173 to see incidents appearing in real-time, categorized by severity.

Once the system is running, you can explore and test the endpoints via the interactive Swagger UI:
 Interactive Docs: http://localhost:8000/docs

IMS (Incident Management System)

Overview: This Incident Management System (IMS) is a distributed-style monitoring system that simulates how modern backend systems handle service signals, process them asynchronously, and display them in a dashboard.

It demonstrates:

->Microservice-style backend design
->Signal ingestion API
->Queue-based processing (Redis simulation)
->Frontend dashboard visualization
->Basic backpressure handling

# Architecture Diagram
            +-------------------+
            |   React Frontend  |
            | (Vite Dashboard)  |
            +-------------------+
                     |
            +-------------------+
            |   FastAPI API     |
            |  /signals endpoint|
            +--------+----------+
                     |
            +-------------------+
            |      Redis        |
            | (Queue Buffer)    |
            +-------------------+
                     |
                     v
            +-------------------+
            | Background Worker |
            | (Async Processor) |
            +-------------------+
                     |
                     v
            +-------------------+
            | In-Memory Store   |
            | (Demo Database)   |
            +-------------------+


# Tech Stack

* Frontend: React (Vite)
* Backend: FastAPI
* Queue: Redis
* Worker: Python background consumer
* Containerization: Docker + Docker Compose

# Setup Instructions



# 1. Clone Repository


git clone https://github.com/<your-username>/ims-system.git
cd ims-system

# 2. Start Full System (Backend + Redis + Worker)

cd infra
docker-compose up --build

This will start:

-> FastAPI backend → `http://localhost:8000`
-> Redis queue
-> Worker service


# 3. Start Frontend
cd frontend
apt npm install
npm run dev


Frontend runs at:

http://localhost:5173

# 4. API Docs

FastAPI Swagger:

http://localhost:8000/docs


# API Usage

# Send Signal

curl -X POST http://localhost:8000/signals \
-H "Content-Type: application/json" \
-d '{"service":"payment","status":"ok"}'


# Get Signals


curl http://localhost:8000/signals




# Backpressure Handling

In distributed systems, backpressure happens when:

-> Incoming requests -> system processing capacity

# How it is handled in this project:
# 1. Redis Queue Buffering

-> All incoming signals are pushed into a Redis queue
-> This prevents API overload

# 2. Worker-Based Processing

->A separate worker consumes messages asynchronously
-> Processing is decoupled from request flow

# 3. Rate Absorption

-> Even if frontend sends spikes of requests:

  -> API responds instantly
  -> Worker processes at its own speed

# 4. Fault Isolation

-> If worker slows down or crashes:

  -> API still accepts requests
  -> Data is safely stored in queue


# Key Learning

1 How message queues prevent system overload
2 Separation of API and processing layer
4 Basic distributed system design principles
5 Frontend-backend integration


# Limitations

1 Uses in-memory storage (not persistent DB)
2 No authentication layer
3 No retry mechanism for failed jobs
4 Basic worker logic (not production-grade)



# Future Improvements

1 Replace in-memory store with PostgreSQL or MongoDB
2 Add retry + dead-letter queue
3 Add authentication (JWT)
4 Deploy using Terraform on AWS
5 Add real-time updates via WebSockets


# Author

Built as a learning project to understand:

1 Distributed systems basics
2 Queue-based architecture
3 Observability concepts
4 Full-stack integration

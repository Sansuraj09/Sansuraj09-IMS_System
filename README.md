# Incident Management System

# Overview
This Incident Management System is a distributed monitoring engine designed to handle high volume service signals, process them asynchronously with debouncing logic, and display them in a real time dashboard.

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
# Project Execution Process:IMS

#1. Infrastructure Provisioning Using Terraform, create the cloud environment for this project, including the AWS EC2 instance and necessary security groups.

    Commands:
            terraform init
            terraform plan
            terraform apply
#2. GitHUb clone: Clone the dedicated GitHub repository to the local environment or EC2 instance to access the application code.

    Commands:
            git clone https://github.com/Sansuraj09/incident-management-system.gi)
            cd incident-management-system
#3. Containerization and Orchestration: Set up the environment using Docker and Docker Compose to manage the frontend, backend, database, and message queue.

    Configuration:
               1 Develop a Dockerfile for the frontend and backend services.
               2 Configure a docker-compose.yaml file to link the FastAPI backend, React/Vite frontend, MongoDB, and Redis.

            Execution:
                       docker compose up -d --build
                       docker ps
               3 Debugging: If services fail to start, inspect the runtime logs:
                       docker logs -f <container_name>
#4. Traffic Simulation Execute simulation scripts to generate incident data and verify system throughput.

    Command:
            python3 scripts/simulate_signals.py
#6. API and Service Verification: Test the individual components to ensure high-volume signals are being processed correctly. API Testing: Verify the signal endpoint using curl.

           curl -X POST http://localhost:8000/signals -H "Content-Type: application/json" -d '{"severity":"P0", "error":"timeout"}'
#Health Check: Ensure the system status is operational.

            curl http://localhost:8000/health
#6. Database Persistence Check: Verify that all incoming signals are being recorded in the MongoDB instance for auditing and analysis.

    Command:
               docker exec -it ims-mongo mongosh
               show bds
               use incident_management_db
               db.raw_signals.find().sort({_id: -1}).limit(1).pretty()
#7. Frontend Visualization: Access the web dashboard to monitor real-time incidents and system health metrics.

    URL: `http://<Public-IP>:5173`
#8. Backend API Root: Access the backend server to verify the core application service and response status.

    URL: http://<Public-IP>:8000/
#9. API Documentation: Access the interactive Swagger UI to review endpoint schemas and perform manual API testing.

    URL: http://<Public-IP>:8000/docs 
#10. Version Control and Maintenance Ensure all configuration and code updates are pushed back to the GitHub repository to maintain project integrity. Action: Regularly commit and push changes to your GitHub account.

        command:
                git add .
                git commit -m "commit_name"
                git push origin main

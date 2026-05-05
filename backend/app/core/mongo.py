from motor.motor_asyncio import AsyncIOMotorClient

# Point to the MongoDB container running in Docker
# Note: If your docker-compose.yml named the service just 'mongo', 
# change 'ims-mongo' to 'mongo' below.
MONGO_URL = "mongodb://ims-mongo:27017" 

# Create the async client
client = AsyncIOMotorClient(MONGO_URL)

# Define and export the specific database you want to use
mongo_db = client.incident_management_db

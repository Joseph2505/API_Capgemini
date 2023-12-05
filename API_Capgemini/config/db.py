from pymongo import MongoClient, ASCENDING
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pymongo')
logger.setLevel(logging.DEBUG)

try:
    conn = MongoClient("mongodb://localhost:27017/capgmini_db")
    # Check if the connection is successful
    conn.server_info()
    # Create an index on the 'siret' field in the 'stock' collection
    conn.capgmini_db.stock.create_index([("siret", ASCENDING)])
    logging.info("Successfully connected to MongoDB.")

except Exception as e:
    logging.error(f"Error connecting to MongoDB: {e}")

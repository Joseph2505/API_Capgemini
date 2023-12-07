from pymongo import MongoClient, ASCENDING
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='mongodb_logs.txt', filemode='a')
logger = logging.getLogger('pymongo')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('mongodb_logs.txt')
logger.addHandler(file_handler)
root_logger = logging.getLogger()
root_logger.addHandler(file_handler)

try:
    conn = MongoClient("mongodb://localhost:27017/capgemini_db")
    # Check if the connection is successful
    conn.server_info()

    logging.info("Successfully connected to MongoDB.")

except Exception as e:
    logging.error(f"Error connecting to MongoDB: {e}")

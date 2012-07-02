from pymongo import Connection
from rq import Queue, use_connection

# PostgreSQL connection for storing user data

# MongoDB connection for storing documents
connection = Connection('localhost', 27017) # Use defaults
document_db = connection.edutext

# Redis connection for creating worker processes
use_connection()
worker_queue = Queue()
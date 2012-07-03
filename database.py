from pymongo import Connection
from rq import Queue, use_connection

connection = Connection('localhost', 27017) # Use defaults
db = connection.test_db
document_db = db.messages

# Redis connection for creating worker processes
use_connection()
worker_queue = Queue()

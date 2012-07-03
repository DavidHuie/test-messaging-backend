import time

from database import document_db, worker_queue

def new_message(*args):
    worker_queue.enqueue(_new_message, *args)

def _new_message(message,
                 author_id,
                 recipient_id):
    """Creates a new message and stores it."""
    message_obj = {'message': message,
                   'author_id': author_id,
                   'recipient_id': recipient_id,
                   'time_updated': time.time()}

    document_db.insert(message_obj)

def get_messages_by_author_id(author_id):
    """Returns all messages by a given author."""
    messages = list(document_db.find({"author_id": author_id}))
    return messages

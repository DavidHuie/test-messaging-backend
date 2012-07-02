from database import document_db, worker_queue


class App(object):
    def __init__(self):
        self.document_db = document_db
        self.worker_queue = worker_queue
import datetime

class Messaging(object):
    def new_message(self,
                    message,
                    message_type,
                    author_id,
                    recipient_id):
        """Creates a new message and stores it."""
        message_obj = {'message': message,
                       'message_type': message_type,
                       'author_id': author_id,
                       'recipient_id': recipient_id,
                       'time_updated': datetime.datetime.utcnow()}

        self.document_db.insert(message_obj)
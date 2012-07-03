import json

from bottle import get, response, run
from gevent import monkey; monkey.patch_all()

from messaging import get_messages_by_author_id, new_message

@get('/messages/author/<author_id>')
def messages_for_author(author_id):
    messages = get_messages_by_author_id(author_id)
    response.content_type = "text/json"
    return json.dumps(messages)

@get('/new_message/<author>/<recipient>/<message>')
def create_message(author, recipient, message):
    new_message(message, author, recipient)

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, server='gevent')

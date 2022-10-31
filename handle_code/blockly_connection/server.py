"""
This module handles the api calls with flask
"""
from flask import Flask, request, jsonify
from handle_code.queue.queue import Queue

APP = Flask("API")

@APP.route('/code', methods=['POST'])
def __post_code():
    """
    This method is called from the Flask application, it handles the incoming post request
    """
    if request.data == "":
        return jsonify(success=False, message="No body was received")
    program = request.data
    queue_length = Queue.add_program_to_queue(program)
    message = "Successfully added your program to the queue"
    return jsonify(
        success=True,
        message=message,
        queueLength=queue_length)

def start_server(port=5000):
    """
    <port> int, optional port to use

    Starts a server which listens on port
    """
    APP.run(port=port, host="0.0.0.0", load_dotenv=False, use_reloader=False)

if __name__ == "__main__":
    # Development
    APP.run(port=5000, host="0.0.0.0", load_dotenv=False, use_reloader=False)

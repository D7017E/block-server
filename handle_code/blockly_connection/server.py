"""
This module handles the api calls with flask
"""
from flask import Flask, request, jsonify
from handle_code import Queue
from handle_code.queue import Program

APP = Flask("API")

@APP.route('/code', methods=['POST'])
def __post_code():
    """
    This method is called from the Flask application, it handles the incoming post request
    """
    if request.data == "":
        return jsonify(success=False, message="No body was received")

    (queue_length, pid, status) = Queue.add_program_to_queue(
        Program(
            request.data,
            request.args.get('name', default="", type=str),
            request.environ['REMOTE_ADDR']
        )
    )
    print(queue_length, pid, status)
    if queue_length == -1 or pid == -1:
        return jsonify(
            success=False,
            message="Program was not added to queue",
            status=status
        )
    return jsonify(
        success=True,
        message="Successfully added your program to the queue",
        queueLength=queue_length,
        pid=pid
    )

@APP.route('/pause', methods=['POST'])
def __pause_execution():
    """
    This method is called from the Flask application, it handles the incoming pause request, and
    makes sure that the queue of programs is not popped from.
    """
    paused = Queue.pause_execution()
    message = "Successfully paused the execution of programs"
    return jsonify(
        success=True,
        message=message,
        paused=paused)

@APP.route('/unpause', methods=['POST'])
def __unpause_execution():
    """
    This method is called from the Flask application, it handles the incoming unpause request, and
    makes sure that the queue of programs is popped from.
    """
    paused = Queue.unpause_execution()
    message = "Successfully unpaused the execution of programs"
    return jsonify(
        success=True,
        message=message,
        paused=paused)

@APP.after_request
def add_header(response):
    """
    Will add headers to every request so that the browser doesn't block the request
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def start_server(port=5000):
    # type: (int) -> None
    """
    <port> int, optional port to use

    Starts a server which listens on port
    """
    APP.run(port=port, host="0.0.0.0", load_dotenv=False, use_reloader=False)

if __name__ == "__main__":
    # Development
    APP.run(port=5000, host="0.0.0.0", load_dotenv=False, use_reloader=False)

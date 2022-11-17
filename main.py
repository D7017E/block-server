"""
Main file, used to initialize connections.
"""
# pylint: disable=superfluous-parens, relative-import, too-many-locals

import time
import threading
import sys
from multiprocessing import Process
# from behaviors.movement.gesture.hip_gesture import HipGesture
from handle_code.code_runner.code_runner import CodeRunner
from handle_code.pepper_connection.pepper_connection import PepperConnection
# from behaviors.expressions.expression import PepperExpression
# from behaviors.movement.gesture.head_gesture import HeadGesture
# from behaviors.movement.gesture.arm_gesture import ArmGesture
# from behaviors.movement.translation.translation import PepperMove
# from behaviors.speech.pepper_speech import PepperSpeech
# from behaviors.composite_functions import CompositeHandler
from handle_code.blockly_connection import server
from handle_code.queue.queue import Queue


class Main(object):
    """
    Main class
    """
    def __init__(self):
        """
        Sets start variables and calls main method.
        """
        self.should_run = True
        self._id = 0
        self.main()

    def main(self):
        """
        Starts a thread for popping programs from the queue, and starts listening on server.
        """
        threading.Thread(target=self.run).start()
        server.start_server(5000)
        print("Interrupted by user, shutting down")
        self.should_run = False
        time.sleep(1.6)
        sys.exit(0)

    def run(self):
        """
        Connects to pepper, and pops programs from the queue.
        """
        while self.should_run:
            time.sleep(1)
            program = Queue.get_next_program()
            if program is not None:
                self._id += 1
                execute_program(program, self._id)
                time.sleep(1)

def execute_program(program, _id):
    """
    Prepare to execute the program
    """
    if program == "":
        return
    max_seconds = 100
    proc = Process(target=__execute_program, args=(program, _id))
    proc.start()
    for _ in range(max_seconds):
        time.sleep(1)
        if not proc.is_alive():
            print("Program has been completed, ready for next task")
            return
    print("Force stopping program")
    proc.terminate()
    proc.join()

def __execute_program(program, _id):
    conn = PepperConnection("130.240.238.32", 9559, "nao", "")
    runner = CodeRunner(_id, program, 60, conn)
    runner.start_execute_program()

Main()

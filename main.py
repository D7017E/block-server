"""
Main file, used to initialize connections.
"""
import os
import time
import threading
import sys
from multiprocessing import Process
from handle_code import CodeRunner, PepperConnection, server, Queue


class Main(object):
    """
    Main class
    """
    def __init__(self):
        """
        Sets start variables and calls main method.
        """
        self.port = 5000
        self.pepper_ip = "130.240.238.32"
        self.pepper_port = 9559
        self.pepper_username = "nao"
        self.should_run = True
        self._id = 0
        self.main()

    def main(self):
        """
        Starts a thread for popping programs from the queue, and starts listening on server.
        """
        if os.environ.get('PORT') is not None:
            self.port = int(os.environ.get('PORT'))
            print(self.port)
        if os.environ.get('PEPPER_IP') is not None:
            self.pepper_ip = os.environ.get('PEPPER_IP')
            print(self.pepper_ip)
        if os.environ.get('PEPPER_PORT') is not None:
            self.pepper_port = int(os.environ.get('PEPPER_PORT'))
            print(self.pepper_port)
        if os.environ.get('PEPPER_USERNAME') is not None:
            self.pepper_username = os.environ.get('PEPPER_USERNAME')
            print(self.pepper_username)

        threading.Thread(target=self.run).start()
        server.start_server(self.port)
        print("Interrupted by user, shutting down")
        self.should_run = False
        time.sleep(1.6)
        sys.exit(0)

    def run(self):
        """
        Connects to pepper, and pops programs from the queue.
        """
        time.sleep(2)
        print("Ready to run programs!")
        while self.should_run:
            time.sleep(1)
            program = Queue.get_next_program()
            if program is not None:
                self._id += 1
                execute_program(
                    program, self._id, self.pepper_ip, self.pepper_port, self.pepper_username
                )
                time.sleep(1)

def execute_program(program, _id, pepper_ip, pepper_port, pepper_username):
    # type: (str, int, str, int, str) -> None
    """
    Prepare to execute the program
    """
    if program == "":
        return
    max_seconds = 100
    proc = Process(target=__execute_program, args=(
        program, _id, pepper_ip, pepper_port, pepper_username
        ))
    proc.start()
    for _ in range(max_seconds):
        time.sleep(1)
        if not proc.is_alive():
            print("Program has been completed, ready for next task")
            return
    print("Force stopping program")
    proc.terminate()
    proc.join()

def __execute_program(program, _id, pepper_ip, pepper_port, pepper_username):
    # type: (str, int, str, int, str) -> None
    conn = PepperConnection(pepper_ip, pepper_port, pepper_username)
    runner = CodeRunner(_id, program, 60, conn)
    runner.start_execute_program()

Main()

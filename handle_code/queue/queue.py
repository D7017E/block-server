"""
This module handles the queue of programs
"""
import threading
from program_object import Program_object as Program

class Queue(object):
    """
    This class is a static class with a list of programs that can
    either be appended to or popped from.
    """
    queue = []
    lock = threading.Lock()
    pause = False
    highest_pid = 0

    @classmethod
    def add_program_to_queue(cls, program):
        # type: (Program, str) -> int
        """
        <program> string, is the program as a string

        A static method which adds a program to the queue
        """
        cls.lock.acquire()
        cls.highest_pid = cls.highest_pid + 1 
        program.set_pid(cls.highest_pid)
        cls.queue.append(program)
        length = len(cls.queue)
        cls.lock.release()
        return length

    @classmethod
    def get_next_program(cls):
        # type: (Queue) -> str | None
        """
        A static method with returns the first value in the queue

        Returns None if there is no more value, otherwise the program string
        """
        if cls.pause:
            return None
        cls.lock.acquire()
        if cls.queue == []:
            cls.lock.release()
            return None
        program = cls.queue.pop(0)
        print(program)
        cls.lock.release()
        return program

    @classmethod
    def pause_execution(cls):
        # type: (Queue) -> bool
        """
        Static method for pausing programs
        """
        cls.pause = True
        return True

    @classmethod
    def unpause_execution(cls):
        # type: (Queue) -> bool
        """
        Static method for unpausing programs
        """
        cls.pause = False
        return False

    @classmethod
    def length(cls):
        # type: (Queue) -> int
        """
        Static method for returning the length of the queue
        """
        return len(cls.queue)

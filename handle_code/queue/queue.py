"""
This module handles the queue of programs
"""
import threading

class Queue(object):
    """
    This class is a static class with a list of programs that can
    either be appended to or popped from.
    """
    queue = []
    lock = threading.Lock()

    @classmethod
    def add_program_to_queue(cls, program):
        # type: (Queue, str) -> None
        """
        <program> string, is the program as a string

        A static method which adds a program to the queue
        """
        cls.lock.acquire()
        cls.queue.append(program)
        length = len(cls.queue)
        cls.lock.release()
        return length

    @classmethod
    def get_next_program(cls):
         # type: (Queue) -> None
        """
        A static method with returns the first value in the queue

        Returns None if there is no more value, otherwise the program string
        """
        cls.lock.acquire()
        if cls.queue == []:
            cls.lock.release()
            return None
        program = cls.queue.pop(0)
        cls.lock.release()
        return program

"""
This module handles the queue of programs
"""
import threading
# pylint: disable=unused-import
import datetime
from typing import Tuple, List
from program_object import Program

class Queue(object):
    """
    This class is a static class with a list of programs that can
    either be appended to or popped from.
    """
    queue = [] # type: List[Program]
    lock = threading.Lock()
    pause = False
    highest_pid = 0
    delta_time = datetime.timedelta(seconds=10)

    @classmethod
    def add_program_to_queue(cls, program):
        # type: (Queue, Program) -> Tuple(int, int, str)
        """
        <program> string, is the program as a string

        A static method which adds a program to the queue
        """
        [should_add, status] = Queue.__should_add_program(program)
        if should_add:
            cls.lock.acquire()
            cls.highest_pid += 1
            pid = cls.highest_pid
            program.set_pid(pid)
            cls.queue.append(program)
            length = len(cls.queue)
            cls.lock.release()
            return (length, pid, status)
        return (-1, -1, status)


    @classmethod
    def get_next_program(cls):
        # type: (Queue) -> None | Program
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
    def __should_add_program(cls, program):
        # type: (Queue, Program) -> Tuple[bool, str]
        """
        *<program> string, is the program as a string

        Checks if the program should be added to the queue by some requirements
        """
        current_time = program.get_timestamp() - cls.delta_time
        cls.lock.acquire()
        for _p in cls.queue:
            if _p.get_ip() == program.get_ip():
                if _p.get_program() == program.get_program():
                    cls.lock.release()
                    return [False, "Program already exists"]
                if current_time < _p.get_timestamp():
                    cls.lock.release()
                    return [False, "Program frequency too high"]
        cls.lock.release()
        return [True, ""]

    @classmethod
    def edit_program(cls, pid, program):
        # type: (Queue, str, str) -> bool
        """
        * <pid> str, program id of the program to edit
        * <program> str, the program text to replace the original program with

        Edits a program based on pid
        """
        for _p in cls.queue:
            if _p.get_pid() == pid:
                _p.set_program(program)
                return True
        return False

    @classmethod
    def get_queue(cls):
        # type: (Queue) -> List[Tuple[str, str]]
        """
        Retrieves the queue as a list of tuples, containing the pid and name of the program.
        """

        result = []
        for _p in cls.queue:
            result.append([_p.get_pid(), _p.get_name()])
        return result

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

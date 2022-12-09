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
    admin_queue = [] # type: List[Program]
    lock = threading.Lock()
    pause = False
    highest_pid = 0
    delta_time = datetime.timedelta(seconds=10)

    @classmethod
    def add_program_to_queue(cls, program):
        # type: (Queue, Program) -> Tuple[int, int, str]
        """
        <program> Program, is the program object to be added to the queue

        A static method which adds a program to the queue
        """
        if program.get_name() == "admin":
            cls.lock.acquire()
            cls.admin_queue.append(program)
            pid = Queue.__increment_pid_add_program(program)
            length = len(cls.admin_queue)
            cls.lock.release()
            return (length, pid, "Added to admin queue")

        [should_add, status] = Queue.__should_add_program(program)
        if should_add:
            cls.lock.acquire()
            pid = Queue.__increment_pid_add_program(program)
            cls.queue.append(program)
            length = len(cls.queue)
            cls.lock.release()
            return (length, pid, status)
        return (-1, -1, status)

    @classmethod
    def __increment_pid_add_program(cls, program):
        # type: (Queue, Program) -> int
        """
        * <program> Program, is the program object

        Will increment the pid and add it to the Program object, returns the pid id
        """
        cls.highest_pid += 1
        program.set_pid(cls.highest_pid)
        return cls.highest_pid

    @classmethod
    def get_next_program(cls):
        # type: (Queue) -> None | Program
        """
        A static method with returns the first value in the queue

        Returns None if there is no more value, otherwise the program string
        """
        program = None
        cls.lock.acquire()
        if cls.admin_queue != []:
            program = cls.admin_queue.pop(0)
        elif not cls.pause and cls.queue != []:
            program = cls.queue.pop(0)
        cls.lock.release()
        return program

    @classmethod
    def __should_add_program(cls, program):
        # type: (Queue, Program) -> Tuple[bool, str]
        """
        *<program> Program, is the program object

        Checks if the program should be added to the queue by some requirements
        """
        current_time = program.get_timestamp() - cls.delta_time
        cls.lock.acquire()
        for _p in cls.queue:
            if _p.get_ip() == program.get_ip():
                if _p.get_program() == program.get_program():
                    cls.lock.release()
                    return (False, "Program already exists")
                if current_time < _p.get_timestamp():
                    cls.lock.release()
                    return (False, "Program frequency too high")
        cls.lock.release()
        return (True, "")

    @classmethod
    def edit_program(cls, pid, program):
        # type: (Queue, int, str) -> bool
        """
        * <pid> int, program id of the program to edit
        * <program> str, the program text to replace the original program with

        Edits a program based on pid
        """
        if pid == -1:
            return False
        cls.lock.acquire()
        for _p in cls.queue:
            if _p.get_pid() == pid:
                _p.set_program(program)
                cls.lock.release()
                return True
        cls.lock.release()
        return False

    @classmethod
    def get_queue(cls):
        # type: (Queue) -> List[Tuple[str, str]]
        """
        Retrieves the queue as a list of tuples, containing the pid and name of the program.
        """

        result = []
        for _p in cls.admin_queue:
            result.append((_p.get_pid(), _p.get_name()))
        for _p in cls.queue:
            result.append((_p.get_pid(), _p.get_name()))
        return result

    @classmethod
    def clear_queue(cls):
        # type: (Queue) -> None
        """
        Clears the queue of all programs
        """
        cls.lock.acquire()
        cls.queue = []
        cls.lock.release()

    @classmethod
    def remove_program(cls, pid):
        # type: (Queue, int) -> Tuple[str, bool]
        """
        Remove a specific program from the queue
        """
        cls.lock.acquire()
        for _i, _p in enumerate(cls.queue):
            if _p.get_pid() == pid:
                cls.queue.pop(_i)
                cls.lock.release()
                return ("Successfully deleted the program from the queue", True)
        cls.lock.release()
        return ("Couldn't find the program", False)

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
    def get_pause(cls):
        # type: (Queue) -> bool
        """
        Static method for getting pause variable
        """
        return cls.pause

    @classmethod
    def length(cls):
        # type: (Queue) -> int
        """
        Static method for returning the length of the queue
        """
        return len(cls.queue)

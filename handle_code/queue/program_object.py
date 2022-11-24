"""
An object to keep track of the programs that are in the queue
"""

import datetime

class Program(object):
    """
    A class which has program specific fields
    """

    def __init__(self, program, name, ip_address):
        # type: (Program, str, str, str) -> None
        """
        * <program> string, is the program string
        * <name> string, is the name of the program
        * <ip_address> string, is the ip address from the sender

        Init for a program object
        """
        self.program = program
        self.name = name
        self.ip_address = ip_address
        self.pid = None
        self.timestamp = datetime.datetime.now()

    def set_pid(self, pid):
        # type: (Program, int) -> None
        """
        * <pid> int, is the pid of the program

        Sets the pid of the program
        """
        self.pid = pid

    def get_pid(self):
        # type: (Program) -> int
        """
        Returns the pid of the program
        """
        return self.pid

    def get_program(self):
        # type: (Program) -> str
        """
        Returns the program string
        """
        return self.program

    def get_name(self):
        # type: (Program) -> str
        """
        Returns the name of the program
        """
        return self.name

    def get_ip(self):
        """
        Returns the ip address from the sender
        """
        return self.ip_address

    def get_timestamp(self):
        """
        Returns the timestamp of when the program was created
        """
        return self.timestamp

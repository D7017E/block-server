

class Program_object(object):

    pid = None

    def __init__(self, program, name, ip_address):
        self.program = program
        self.name = name
        self.ip_address = ip_address

    def set_pid(self, pid):
        self.pid = pid
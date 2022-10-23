import threading

class Queue(object):
    queue = []
    lock = threading.Lock()
    
    @classmethod
    def add_program_to_queue(self, program):
        """
        <program> string, is the program as a string
        
        A static method which adds a program to the queue
        """
        print(self.queue)
        self.lock.acquire()
        self.queue.append(program)
        length = len(self.queue)
        self.lock.release()
        return length

    @classmethod
    def get_next_program(self):
        """
        A static method with returns the first value in the queue
        
        Returns None if there is no more value, otherwise the program string
        """
        self.lock.acquire()
        if len(self.queue) == 0:
            self.lock.release()
            return None
        program = self.queue.pop(0)
        self.lock.release()
        return program
    

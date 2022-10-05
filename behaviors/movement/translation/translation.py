import random
import time
import threading

class PepperMove():

    def __init__(self, service):
        self.stop_id = None
        self.service = service
        self.thread = None
        self.lock = threading.Lock()

    def move(self, x, y, angle, duration):
        """
        Move which takes in a
        * x speed, positive means forward, negative means backward [-0.35, 0.35]
        * y speed, positive means left, negative means right [-0.35, 0.35]
        * angle speed, positive means rotate left, negative means rotate right [-1, 1]
        * duration in seconds. It is the duration of how long the movement should happen

        x and y max speed is 0.35 which is 35 cm per second.
        Meaning that if setting the timeout to 3 it moves 105 cm forward, (0.35 * 3)
        
        Angle max speed is about 58 degrees per second, but is set as percentage.
        1 is 58 degrees per second. passing in 6.25s, then the robot will do one revolution
        """

        # set moving speed
        self.service.move(x, y, angle)
        stop_id = random.randint(0, 1000000)
        # acquire lock for stop id and thread
        self.lock.acquire()
        self.stop_id = stop_id
        if self.thread is not None:
            self.thread.join()
        self.thread = threading.Thread(
            target=self.__stop_movement,
            args=(stop_id, duration))
        self.thread.start()
        self.lock.release()

    def stop_movement(self):
        """
        Will stop movement right away and stop all treads running
        """
        self.service.move(0, 0, 0)
        self.lock.acquire()
        if self.thread is not None:
            self.thread.join()
        self.stop_id = None
        self.lock.release()

    def __stop_movement(self, stop_id, timeout):
        time.sleep(timeout)
        self.lock.acquire()
        if stop_id == self.stop_id:
            self.service.move(0, 0, 0)
        self.lock.release()

import random
import time

class PepperMove():

    def __init__(self):
        self.stop_id = None

    def move(self, service, x, y, angle, timeout):
        service.move(x, y, angle)
        stop_id = random.randint(0, 1000000)
        self.stop_id = stop_id
        time.sleep(timeout)
        self.__stopMovement(service, stop_id)

    def stopMovement(self, service):
        service.move(0, 0, 0)
    
    def __stopMovement(self, service, stop_id):
        if stop_id == self.stop_id:
            service.move(0, 0, 0)
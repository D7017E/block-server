import time
import threading

class PepperExpression():

    def __init__(self, startColor, service):
        self.previousColor = startColor
        self.service = service
        service.createGroup(
            "BlinkGroup",
            [
                "FaceLed0",
                "FaceLed1",
                "FaceLed3",
                "FaceLed4",
                "FaceLed5",
                "FaceLed7",
            ]
        )

    def rotate_eyes(self, rgb):
        self.previousColor = rgb
        self.service.rotateEyes(rgb, 1, 5)

    def fade_eyes(self, rgb, duration):
        self.previousColor = rgb
        self.service.fadeRGB("FaceLeds", rgb, duration)

    def close_eyes(self):
        self.service.fadeRGB("BlinkGroup", 0x000000, 0.10)

    def open_eyes(self): 
        self.service.fadeRGB("FaceLeds", self.previousColor, 0.10)

    def blink_eyes(self, duration):
        self.close_eyes()
        time.sleep(duration)
        self.open_eyes()

    def random_eyes(self, duration):
        self.service.randomEyes(duration)
        self.fade_eyes(self.previousColor, 1)
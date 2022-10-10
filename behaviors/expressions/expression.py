import time

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
        service.createGroup(
            "AngryEyesGroup",
            [
                "FaceLed2",
                "FaceLed3",
                "FaceLed4",
                "FaceLed5",
                "FaceLed6",
                "FaceLed7",
            ]
        )
        service.createGroup(
            "-AngryEyesGroup",
            [
                "FaceLed0",
                "FaceLed1",              
            ]
        )


    def rotate_eyes(self, rgb):
        """
        * <rgb> the hexadecimal color value that the rotating part of the eyes should be. Example: 0x000000 for white.

        Makes a color rotate around the eyes. 
        """
        self.previousColor = rgb
        self.service.rotateEyes(rgb, 1, 5)

    def fade_eyes(self, rgb, duration):
        """
        * <rgb> the hexadecimal color value that the eyes should be faded to. Example: 0x000000 for white. 
        * <duration> time in seconds that determine how fast the eyes will fade in.

        Sets both eyes to a certain color, with a fade in time of duration.
        """
        self.previousColor = rgb
        self.service.fadeRGB("FaceLeds", rgb, duration)

    def angry_eyes(self):
        """
        Makes part of the eyes red, and the upper two leds black.
        """
        self.service.fadeRGB("AngryEyesGroup", 0xff0000, 0.10)
        self.service.fadeRGB("-AngryEyesGroup", 0x000000, 0.10)
    def sad_eyes(self):
        """
        Makes the eyes blue.
        """
        self.fade_eyes(0x0000ff, 1)

    def __close_eyes(self):
        self.service.fadeRGB("BlinkGroup", 0x000000, 0.10)

    def __open_eyes(self): 
        self.service.fadeRGB("FaceLeds", self.previousColor, 0.10)

    def blink_eyes(self, duration):
        """
        * <duration> time in seconds that the eyes should stay closed.

        Sets both eyes to black, and then sleeps for duration.
        Afterwards it sets both eyes to self.previousColor.
        """
        self.__close_eyes()
        time.sleep(duration)
        self.__open_eyes()
    
    def squint_eyes(self, duration):
        """
        * <duration> time in seconds that the eyes should squint for.

        Makes Pepper squint for duration.
        """
        self.service.fadeRGB("SquintGroup", 0x000000, 1)
        time.sleep(duration)
        self.service.fadeRGB("SquintGroup", self.previousColor, 1)
        # self.open_eyes()

    def random_eyes(self, duration):
        """
        * <duration> time in seconds that the eye leds should be randomized.

        Sets every eye led to a random value for the duration.
        Afterwards fades to self.previousColor.
        """
        self.service.randomEyes(duration)
        self.fade_eyes(self.previousColor, 1)
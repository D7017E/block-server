"""
File for gesticulating the arms of Pepper.
"""

class ArmGesture():
    """
    Class for gesticulating the arms of pepper.
    """

    def __init__(self, service):
        """
        * <service>, a motion_service from naoqi.
        Initializes the ArmGesture object.
        """
        self.service = service

    def move_left_arm(self, roll, speed, degrees):
        """
        * <roll> boolean, indicates whether the axis of movement is roll (true) or pitch (false).
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to.
        Moves the left arm to a certain angle with a certain speed.
        """
        if speed <= 0 or speed > 100:
            print("Wrong input for speed, only accepts (0, 100]")
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 35%
        if roll is True:
            if degrees < 0.5 or degrees > 89.5:
                print("wrong input for angle, only accepts [0.5, 89.5]")
                return
            angle = degrees * 3.14 / 180
            self.service.setAngles("LShoulderRoll", angle, speed)
        else:
            if degrees < -119.5 or degrees > 119.5:
                print("wrong input for angle, only accepts [-119.5, 119.5]")
                return
            angle = degrees * 3.14 / 180
            self.service.setAngles("LShoulderPitch", angle, speed)

    def move_right_arm(self, roll, speed, degrees):
        """
        * <roll> boolean, indicates whether the axis of movement is roll (true) or pitch (false).
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to.
        Moves the right arm to a certain angle with a certain speed.
        """
        if speed <= 0 or speed > 100:
            print("Wrong input for speed, only accepts (0, 100]")
            return
        speed = float(speed) * 0.002 # 0.0035 # to remove percentage and restrict max speed to 35%
        if roll is True:
            if degrees < -89.5 or degrees > -0.5:
                print("wrong input for angle, only accepts [-0.5, -89.5]")
                return
            angle = degrees * 3.14 / 180
            self.service.setAngles("RShoulderRoll", angle, speed)
        else:
            if degrees < -119.5 or degrees > 119.5:
                print("wrong input for angle, only accepts [-119.5, 119.5]")
                return
            angle = degrees * 3.14 / 180
            self.service.setAngles("RShoulderPitch", angle, speed)

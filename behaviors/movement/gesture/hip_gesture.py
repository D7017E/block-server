"""
File for gesticulating the hips of Pepper.
"""
#pylint: disable=superfluous-parens, too-few-public-methods, relative-import

from arm_gesture import check_speed

class HipGesture(object):
    """
    Class for gesticulating the hips of Pepper.
    """

    def __init__(self, service):
        """
        * <service>, a motion_service from naoqi.
        Initializes the HipGesture object.
        """
        self.service = service

    def rotate_hip_roll(self, speed, angle):
        # type: (HipGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-29.5, 29.5].

        Rotates the hip's roll to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 35%
        if angle < -29.5 or angle > 29.5:
            print("wrong input hip_roll's angle, only accepts [-29.5, 29.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("HipRoll", angle, speed)

    def rotate_hip_pitch(self, speed, angle):
        # type: (HipGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-59.5, 59.5].

        Rotates the hip's pitch to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 35%
        if angle < -59.5 or angle > 59.5:
            print("wrong input hip_pitch's angle, only accepts [-59.5, 59.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("HipPitch", angle, speed)


    def reset_hip(self):
        """
        Resets the hips to their default position.
        """
        self.rotate_hip_roll(75, 0)
        self.rotate_hip_pitch(75, -10)

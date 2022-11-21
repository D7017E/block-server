"""
File for gesticulating the arms of Pepper.
"""

#pylint: disable=superfluous-parens

class ArmGesture(object):
    """
    Class for gesticulating the arms of pepper.
    """

    def __init__(self, service):
        """
        * <service>, a motion_service from naoqi.
        Initializes the ArmGesture object.
        """
        self.service = service

    def rotate_left_shoulder_roll(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [0.5, 89.5].
        Rotates the left shoulders's roll to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < 0.5 or angle > 89.5:
            print("wrong input left_shoulder_roll's angle, only accepts [0.5, 89.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("LShoulderRoll", angle, speed)

    def rotate_left_shoulder_pitch(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-119.5, 119.5].
        Rotates the left shoulders's pitch to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < -119.5 or angle > 119.5:
            print("wrong input left_shoulder_pitch's angle, only accepts [-119.5, 119.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("LShoulderPitch", angle, speed)

    def rotate_left_elbow_roll(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-89.5, -0.5].
        Rotates the left elbows's roll to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < -89.5 or angle > -0.5:
            print("wrong input left_elbow_roll's angle, only accepts [-89.5, -0.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("LElbowRoll", angle, speed)

    def rotate_left_elbow_yaw(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-119.5, 119.5].
        Rotates the left elbows's yaw to a certain angle with a certain speed.
        NOTE: Does not need to be implemented on blockly site.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < -119.5 or angle > 119.5:
            print("wrong input left_elbow_yaw's angle, only accepts [-119.5, 119.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("LElbowYaw", angle, speed)

    def rotate_right_shoulder_roll(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-0.5, -89.5].
        Rotates the right shoulders's roll to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < -89.5 or angle > -0.5:
            print("wrong input right_shoulder_roll's angle, only accepts [-0.5, -89.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("RShoulderRoll", angle, speed)

    def rotate_right_shoulder_pitch(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-119.5, 119.5].
        Rotates the right shoulders's pitch to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < -119.5 or angle > 119.5:
            print("wrong input right_shoulder_pitch's angle, only accepts [-119.5, 119.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("RShoulderPitch", angle, speed)

    def rotate_right_elbow_roll(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [0.5, 89.5].
        Rotates the right elbows's roll to a certain angle with a certain speed.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < 0.5 or angle > 89.5:
            print("wrong input right_elbow_roll's angle, only accepts [0.5, 89.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("RElbowRoll", angle, speed)

    def rotate_right_elbow_yaw(self, speed, angle):
        # type: (ArmGesture, int, float) -> None
        """
        * <speed> integer, the speed at which the movement occurs. Between [0, 100].
        * <degrees> integer, the angle which the arm should move to. Between [-119.5, 119.5].
        Rotates the right elbows's yaw to a certain angle with a certain speed.
        NOTE: Does not need to be implemented on blockly site.
        """
        if not check_speed(speed):
            return
        speed = float(speed) * 0.002 # to remove percentage and restrict max speed to 20%
        if angle < -119.5 or angle > 119.5:
            print("wrong input right_elbow_yaw's angle, only accepts [-119.5, 119.5]")
            return
        angle = angle * 3.14 / 180
        self.service.setAngles("RElbowYaw", angle, speed)

    def reset_arms(self):
        # type: (ArmGesture) -> None
        """
        Resets arms to start position.
        """
        self.rotate_right_shoulder_roll(100, -.5)
        self.rotate_left_shoulder_roll(100, .5)
        self.rotate_right_shoulder_pitch(100, 90)
        self.rotate_left_shoulder_pitch(100, 90)
        self.rotate_left_elbow_roll(100, -.5)
        self.rotate_right_elbow_roll(100, .5)
        self.rotate_right_elbow_yaw(100, 0)
        self.rotate_left_elbow_yaw(100, 0)

def check_speed(speed):
    # type: (int) -> bool
    """
    Ensures that the speed parameter is within range.
    """
    if speed <= 0 or speed > 100:
        print("Wrong input for speed, only accepts (0, 100]")
        return False
    return True

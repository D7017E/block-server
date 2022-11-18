"""
A file for composite functions, like dance and poses.
"""

import time

class CompositeHandler(object):
    """
    A class for composite functions, like dance and poses.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, arms, head, mouth, eyes, hips):
        """
        Initializes the CompositeHandler object.
        """
        # type: (ArmGesture, HeadGesture, PepperSpeech, PepperExpression, HipGesture) -> None
        self.arms = arms
        self.head = head
        self.mouth = mouth
        self.eyes = eyes
        self.hips = hips

    def dance(self):
        """
        Makes Pepper dance.
        """
        self.robot_arms()
        self.ketchup_arms()

    def ketchup_arms(self):
        """
        Do the ketchup dance.
        """
        self.arms.rotate_right_shoulder_pitch(100, 20)
        self.arms.rotate_left_shoulder_pitch(100, -20)

        time.sleep(1)

        self.arms.rotate_right_elbow_yaw(100, 0)
        self.arms.rotate_left_elbow_yaw(100, 0)

        time.sleep(1)

        switch = True

        i = 0
        while i < 8:
            if i % 2 == 0:
                switch = not switch

            self.arms.rotate_right_shoulder_pitch(100, -20 if switch else 20)
            self.arms.rotate_left_shoulder_pitch(100, 20 if switch else -20)

            time.sleep(0.5)

            self._ketchup_arm_help()

            i += 1

        self.eyes.fade_eyes(0xffffff, 1)
        self.arms.reset_arms()



    def _ketchup_arm_help(self):
        self.arms.rotate_right_elbow_roll(100, 65)
        self.arms.rotate_left_elbow_roll(100, -65)
        self.eyes.fade_eyes(0x00ff00, 0.5)

        time.sleep(0.5)

        self.arms.rotate_right_elbow_roll(100, 0.5)
        self.arms.rotate_left_elbow_roll(100, -0.5)
        self.eyes.fade_eyes(0x0000ff, 0.5)

        time.sleep(0.5)


    def robot_arms(self):
        """
        Makes Pepper dance like a robot.
        """
        self.arms.rotate_right_shoulder_pitch(100, 0)
        self.arms.rotate_left_shoulder_pitch(100, 0)

        self.arms.rotate_right_elbow_yaw(100, -90)
        self.arms.rotate_left_elbow_yaw(100, 90)

        self.arms.rotate_right_shoulder_roll(100, -89.5)
        self.arms.rotate_left_shoulder_roll(100, 89.5)

        time.sleep(0.5)
        i = 0
        while i < 8:

            self.arms.rotate_right_elbow_roll(100, 89)
            self.arms.rotate_left_elbow_roll(100, -0.5)
            self.hips.rotate_hip_roll(10, 69)

            time.sleep(1)

            self.arms.rotate_right_elbow_roll(100, 0.5)
            self.arms.rotate_left_elbow_roll(100, -89)
            self.hips.rotate_hip_roll(-10, 69)

            time.sleep(1)

            i += 1

        self.hips.rotate_hip_roll(0, 100)
        self.arms.reset_arms()

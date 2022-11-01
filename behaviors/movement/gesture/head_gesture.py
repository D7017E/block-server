"""
Class for gesticulating the head.
"""

import time
import threading

class HeadGesture(object):
    """
    Class for gesticulating the head.
    """

    def __init__(self, service):
        """
        * <service>, a motion_service from naoqi.
        Initializes the HeadGesture object.
        """
        self.service = service
        self.spinning_head_running = False

    def move_head(self, yaw, degrees, speed):
        """
        * <yaw> boolean, if True then we change the yaw (left, right) else pitch (up, down)
        * <degrees>, if yaw between [-119.5, 119.5] (right and left) |
                  if pitch between [-40.5, 20.5] (up and down)
        * <speed>, between (0, 100]. Equal to percentage of max speed
        Moves the head in the direction given by parameters
        """
        if speed <= 0 or speed > 100:
            print("Wrong input for speed, only accepts (0, 100]")
            return
        speed = float(speed) * 0.0035 # to remove percentage and restrict max speed to 35%
        if yaw is True:
            if degrees < -119.5 or degrees > 119.5:
                print("wrong input for angle, only accepts [-119.5, 119.5]")
                return
            angle = degrees * 3.14 / 180
            self.service.setAngles("HeadYaw", angle, speed)
        else:
            if degrees < -40.5 or degrees > 20.5:
                print("wrong input for angle, only accepts [-40.5, 20.5]")
                return
            angle = degrees * 3.14 / 180
            self.service.setAngles("HeadPitch", angle, speed)

    def reset_head(self):
        """
        Resets the head position to 0, 0 for Pepper
        """
        self.move_head(True, 0, 70)
        self.move_head(False, 0, 70)

    def nod_head(self):
        """
        Nods the head up and down, this method takes about 1.6 seconds
        """
        self.reset_head()
        time.sleep(0.4)
        self.move_head(False, -20, 70)
        time.sleep(0.4)
        self.move_head(False, 10, 100)
        time.sleep(0.4)
        self.move_head(False, -20, 100)
        time.sleep(0.4)
        self.reset_head()

    def shake_head(self):
        """
        Shakes the head side to side, this method takes about 3 seconds
        """
        self.reset_head()
        time.sleep(0.5)
        self.move_head(True, 45, 100)
        time.sleep(0.5)
        self.move_head(True, -45, 100)
        time.sleep(1)
        self.move_head(True, 45, 100)
        time.sleep(1)
        self.reset_head()

    def spin_head(self, duration):
        """
        * <duration> is the number of seconds that the head should spin
        Spins the head up and down, side to side
        """
        if self.spinning_head_running:
            print("Spinning head is already running")
            return
        self.spinning_head_running = True
        self.reset_head()
        time.sleep(0.3)
        thread = threading.Thread(
            target=self.__do_spin_head,
            args=()
        )
        thread.start()
        time.sleep(duration)
        self.spinning_head_running = False
        time.sleep(0.1)
        self.reset_head()

    def __do_spin_head(self):
        yaw = 0
        yaw_step = 20
        pitch = 0
        pitch_step = 10
        yaw_direction = 1
        pitch_direction = 1
        while self.spinning_head_running:
            yaw += yaw_step * yaw_direction
            pitch += pitch_step * pitch_direction
            if yaw < -119.5 or yaw > 119.5:
                yaw_direction = -yaw_direction
                yaw += yaw_step * yaw_direction
            if pitch < -40.5 or pitch > 20.5:
                pitch_direction = -pitch_direction
                pitch += pitch_step * pitch_direction
            self.move_head(True, yaw, 40)
            self.move_head(False, pitch, 40)
            time.sleep(0.1)

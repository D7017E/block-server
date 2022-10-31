

class Arm_gesture():
    
    def __init__(self, service):
        self.service = service
    
    def move_left_arm(self, roll, speed, degrees):
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
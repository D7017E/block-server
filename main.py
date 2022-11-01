"""
Main file, used to initialize connections.
"""


import time
import os
import threading
import sys
from numpy import empty
from PepperConnection import PepperConnection
from behaviors.expressions.expression import PepperExpression
from behaviors.movement.gesture.head_gesture import HeadGesture
from behaviors.movement.gesture.arm_gesture import ArmGesture
from behaviors.movement.translation.translation import PepperMove
# from behaviors.speech.PepperSpeech import PepperSpeech
from handle_code.blockly_connection import server
from handle_code.queue.queue import Queue

class Main:
    """
    Main class
    """
    def __init__(self):
        """
        Sets start variables and calls main method.
        """
        self.should_run = True
        self.connect_to_pepper = True
        self.main()

    def main(self):
        """
        Starts a thread for popping programs from the queue, and starts listening on server.
        """
        threading.Thread(target=self.run).start()
        server.start_server(5020)
        print("Interrupted by user, shutting down")
        self.should_run = False
        time.sleep(1.6)
        sys.exit(0)

    def run(self):
        """
        Connects to pepper, and pops programs from the queue.
        """
        if self.connect_to_pepper:
            conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password"))

            conn.connect()

            # tts_service = conn.get_speech_service()
            motion_service = conn.get_motion_service()
            auto_service = conn.get_autonomous_service()
            battery_service = conn.get_battery_service()
            # led_service = conn.get_led_service()
            # audio_service = conn.get_audio_service()
            # tablet_service = conn.get_tablet_service()
            behavior_service = conn.get_behavior_service()
            blinking_service = conn.get_blinking_service()
            # default state is "interactive"
            auto_service.setState("safeguard")
            motion_service.setIdlePostureEnabled("Head", False)
            auto_service.stopAll()
            behavior_service.stopAllBehaviors()
            blinking_service.setEnabled(False)
            print(blinking_service.isEnabled())
            # print(ret)
            # auto_service.setState("interactive")
            print(auto_service.getState())
            print(auto_service.focusedActivity())
            print(auto_service.getAutonomousActivityStatistics())
            print("battery level is: {}%".format(battery_service.getBatteryCharge()))
            # auto_service.stopFocus()
            print(auto_service.focusedActivity())
            # arm_ges.move_left_arm(False, 100, 90)
            # arm_ges.move_right_arm(False, 100, 90)
            # ges.reset_head()
            # threading.Thread(target=ges.spin_head, args=(10,)).start()
            pep_expr = PepperExpression(0xffffff, conn.get_led_service())
            # pepExpr.random_eyes(10)


            # move_service.setOrthogonalSecurityDistance(0.4)
            # move_service.move(0.25,0,0)
            # time.sleep(3)
            # move_service.move(0,0,0)
            # return
            pep_expr.angry_eyes()
            head_ges = HeadGesture(motion_service)
            head_ges.reset_head()


            pepper_move = PepperMove(motion_service)
            pepper_move.move(0, 0, 0.5, 3)
            time.sleep(2.5)
            pepper_move.move(0, 0, 1, 10)

            arm_ges = ArmGesture(motion_service)
            arm_ges.move_left_arm(True, 100, 89.5)
            time.sleep(0.1)
            arm_ges.move_right_arm(True, 100, -89.5)
            # pepperMove.move(0.2, -0.1, 1, 10)


            # pepExpr.fade_eyes(0xffffff, 1)
            # pepExpr.rotate_eyes(0xffffff)
            # pepExpr.wink_eye("right")

            # pepExpr.fade_eyes(led_service, 0xff0000, 1)
            # pepExpr.random_eyes(5)
            # pepExpr.squint_eyes(1)
            # pepExpr.blink_eyes(0.10)
        while self.should_run:
            time.sleep(1)
            program = Queue.get_next_program()
            if program is not None:
                execute_program(program)
        if self.connect_to_pepper:
            print("Resetting pepper")
            head_ges.reset_head()
            arm_ges.move_left_arm(True, 100, 0.5)
            arm_ges.move_right_arm(True, 100, -0.5)
            arm_ges.move_left_arm(False, 100, 90)
            arm_ges.move_right_arm(False, 100, 90)
            pep_expr.fade_eyes(0xffffff, 1)
            pepper_move.stop_movement()
            time.sleep(0.4)

def execute_program(program):
    """
    Executes a program with the help of exec.
    """
    if program is empty:
        return
    # TODO: Do something before? Add some timer? Run in thread? Check code?
    exec(program) # pylint: disable=exec-used
    time.sleep(5)

Main()

from PepperConnection import PepperConnection
from behaviors.expressions.expression import PepperExpression
from behaviors.movement.gesture.gesture import Gesture
from behaviors.movement.translation.translation import PepperMove
from behaviors.speech.PepperSpeech import PepperSpeech
from handle_code.blockly_connection import server
from handle_code.queue.queue import Queue
import time
import os
import threading
import sys

class Main:
    def __init__(self):
        self.should_run = True
        self.connectToPepper = False
        self.main()

    def main(self):
        threading.Thread(target=self.run).start()
        server.start_server(5000)
        print("Interrupted by user, shutting down")
        self.should_run = False
        time.sleep(1.6)
        sys.exit(0)

    def run(self):
        if self.connectToPepper:
            conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password"))

            conn.connect()

            tts_service = conn.get_speech_service()
            motion_service = conn.get_motion_service()
            auto_service = conn.get_autonomous_service()
            battery_service = conn.get_battery_service()
            led_service = conn.get_led_service()
            audio_service = conn.get_audio_service()
            tablet_service = conn.get_tablet_service()
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
            
            ges = Gesture(motion_service)
            ges.reset_head()
            # threading.Thread(target=ges.spin_head, args=(10,)).start()
            pepExpr = PepperExpression(0xffffff, led_service)
            # pepExpr.random_eyes(10)

            
            # move_service.setOrthogonalSecurityDistance(0.4)
            # move_service.move(0.25,0,0)
            # time.sleep(3)
            # move_service.move(0,0,0)
            # return

            pepperMove = PepperMove(motion_service)
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
                    self.executeProgram(program)
        if self.connectToPepper:
            print("Resetting pepper")
            ges.reset_head()
            pepExpr.fade_eyes(0xffffff, 1)
            pepperMove.stop_movement()
            time.sleep(0.4)
    
    def executeProgram(self, program):
        if len(program) == 0:
            return
        # TODO: Do something before? Add some timer? Run in thread? Check code?
        exec(program)
        time.sleep(5)

Main()
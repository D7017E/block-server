from shutil import move
from PepperConnection import PepperConnection
from behaviors.expressions.expression import PepperExpression
from behaviors.movement.gesture.gesture import Gesture
from behaviors.movement.translation.translation import PepperMove
from behaviors.speech.PepperSpeech import PepperSpeech
import time
import os
import threading

def main():

    conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password"))

    conn.connect()

    tts_service = conn.get_speech_service()
    motion_service = conn.get_motion_service()
    auto_service = conn.get_autonomous_service()
    battery_service = conn.get_battery_service()
    led_service = conn.get_led_service()
    
    # default state is "interactive"
    auto_service.setState("safeguard")
    # auto_service.setState("interactive")
    print(auto_service.getState())
    print(auto_service.focusedActivity())
    print(auto_service.getAutonomousActivityStatistics())
    print("battery level is: {}%".format(battery_service.getBatteryCharge()))
    # auto_service.stopFocus()
    print(auto_service.focusedActivity())
    
    ges = Gesture(motion_service)
    threading.Thread(target=ges.spin_head, args=(10,)).start()
    pepExpr = PepperExpression(0xffffff, led_service)
    pepExpr.random_eyes(10)
    
    # move_service.setOrthogonalSecurityDistance(0.4)
    # move_service.move(0.25,0,0)
    # time.sleep(3)
    # move_service.move(0,0,0)
    # return

    # pepperMove = PepperMove(move_service)
    # pepperMove.move(0.2, -0.1, 1, 10)

    # pepExpr = PepperExpression(0xffffff, led_service)
    # pepExpr.fade_eyes(led_service, 0xff0000, 1)
    # pepExpr.random_eyes(5)
    # pepExpr.blink_eyes(0.10)
    # while True:
    #     time.sleep(1)
    # move_service.move(0,0,0)

main()
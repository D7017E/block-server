from shutil import move
from PepperConnection import PepperConnection
from behaviors.movement.translation.translation import PepperMove
from behaviors.expressions.expression import PepperExpression
from behaviors.speech.PepperSpeech import PepperSpeech
import time

def main():

    conn = PepperConnection("130.240.238.32", 9559, "nao", "FBLovesLMS2019")

    conn.connect()

    tts_service = conn.get_speech_service()
    move_service = conn.get_move_service()
    auto_service = conn.get_autonomous_service()
    led_service = conn.get_led_service()
    battery_service = conn.get_battery_service()
    
    # default state is "interactive"
    auto_service.setState("safeguard")
    # auto_service.setState("interactive")
    print(auto_service.getState())
    print(auto_service.focusedActivity())
    print(auto_service.getAutonomousActivityStatistics())
    print("battery level is: {}%".format(battery_service.getBatteryCharge()))
    # auto_service.stopFocus()
    print(auto_service.focusedActivity())

    move_service.setOrthogonalSecurityDistance(0.2)
    # pepperMove = PepperMove(move_service)
    # pepperMove.move(0.2, -0.1, 1, 10)

    pepExpr = PepperExpression(0xffffff, led_service)
    # pepExpr.fade_eyes(led_service, 0xff0000, 1)
    # pepExpr.random_eyes(5)
    pepExpr.blink_eyes(0.10)
    while True:
        time.sleep(1)
    

main()
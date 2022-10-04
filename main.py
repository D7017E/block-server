from shutil import move
from PepperConnection import PepperConnection
from behaviors.movement.translation.translation import PepperMove
from behaviors.speech.PepperSpeech import PepperSpeech
import time

def main():

    conn = PepperConnection("130.240.238.32", 9559, "nao", "FBLovesLMS2019")

    conn.connect()

    tts_service = conn.get_speech_service()
    move_service = conn.get_move_service()
    auto_service = conn.get_autonomous_service()
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
    while True:
        time.sleep(1)
    # move_service.move(0,0,0)

main()
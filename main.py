from PepperConnection import PepperConnection
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
    
    # default state is "interactive"
    auto_service.setState("safeguard")
    print(auto_service.getState())

    # move_service.setOrthogonalSecurityDistance(0.4)
    # move_service.move(0.25,0,0)
    # time.sleep(3)
    # move_service.move(0,0,0)
    # return

    # for i in range(10):
    #     move_service.move(0, 0, 1)
    #     time.sleep(0.1)
    # return
    pepExpr = PepperExpression(0xffffff, led_service)
    # pepExpr.fade_eyes(led_service, 0xff0000, 1)
    # pepExpr.random_eyes(5)
    pepExpr.blink_eyes(0.10)
    # PepperExpression().fade_eyes(led_service, 0xffffff, 3)
    # PepperExpression().rotate_eyes(led_service, 0x00ff0000)
    # PepperSpeech().talk(tts_service, "Hello, world!")
    # while True:
    #     inp = raw_input("Enter text: ")

    #     tts_service.say(
    #         ("\\RSPD={0}\\ \\VCT={1} \\" + str(inp)).format(100, 100)
    #     )
    

main()
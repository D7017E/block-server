"""
Code runner module which handles the code execution of programs
"""
import threading
import time
from behaviors.movement.gesture.hip_gesture import HipGesture
from handle_code.pepper_connection.pepper_connection import PepperConnection
from behaviors.expressions.expression import PepperExpression
from behaviors.movement.gesture.head_gesture import HeadGesture
from behaviors.movement.gesture.arm_gesture import ArmGesture
from behaviors.movement.translation.translation import PepperMove
from behaviors.speech.pepper_speech import PepperSpeech
from behaviors.composite_functions import CompositeHandler

class ExecInterrupt(Exception):
    pass

class CodeRunner(object):
    def __init__(self, program_id, program, timeout_program, conn):
        # type: (int, str, int, PepperConnection) -> CodeRunner
        self.program_id = program_id
        self.program = self.__process_program(program)
        print(self.program)
        self.timeout_program = timeout_program
        self.conn = conn
        self.should_exit = False
        self.connecting = False
        self.program_exited = False

    def start_execute_program(self):
        self.__connect_to_pepper_timer(10)
        self.__reset_pepper()
        self.__execute_program()
        self.__reset_pepper()
        self.auto_service.setState("interactive")
        time.sleep(2)

    def __process_program(self, program):
        # type: (str) -> None
        return program.replace("\n", "\nif self.should_exit:\n    raise ExecInterrupt\n")

    def __execute_program(self):
        self.should_exit = False
        threading.Thread(target=self.__exec).start()
        for _ in range(self.timeout_program):
            time.sleep(1)
            if self.program_exited:
                return
        self.should_exit = True
        time.sleep(3)
        self.__reset_pepper()
        time.sleep(2)
        raise StopIteration("Force quit Pepper execution")

    def __exec(self):
        self.__print("Running the program")
        try:
            exec(self.program)
        except ExecInterrupt as e:
            pass
        except Exception as e:
            self.__print("Execution error: " + str(e))
            self.program_exited = True
            return
        self.__print("Stopping the program")
        time.sleep(3)
        self.program_exited = True

    def __connect_to_pepper_timer(self, timer):
        # type: (int) -> None
        self.connecting = True
        threading.Thread(target=self.__configure_and_connect_to_pepper).start()
        for _ in range(timer):
            time.sleep(1)
            if not self.connecting:
                return

        self.__print("Timeout when connecting to pepper")
        raise ConnectionError("Timeout when connecting to pepper")
    
    def __reset_pepper(self):
        self.__print("Resetting Pepper")
        self.head_ges.reset_head()
        self.arm_ges.reset_arms()
        self.hip_ges.reset_hip()
        self.pep_move.stop_movement()
        time.sleep(1.5)
        self.__print("Done with resetting Pepper")

    def __configure_and_connect_to_pepper(self):
        """
        Configure a connection and services
        """
        self.__print("Trying to connect to Pepper")
        self.conn.connect()
        time.sleep(1)
        self.tts_service = self.conn.get_speech_service()
        self.motion_service = self.conn.get_motion_service()
        self.auto_service = self.conn.get_autonomous_service()
        self.behavior_service = self.conn.get_behavior_service()
        self.blinking_service = self.conn.get_blinking_service()

        # default state is "interactive"
        self.auto_service.setState("safeguard")
        self.motion_service.setIdlePostureEnabled("Head", False)
        self.auto_service.stopAll()
        self.behavior_service.stopAllBehaviors()
        self.blinking_service.setEnabled(False)

        self.pep_speech = PepperSpeech(self.tts_service)
        self.head_ges = HeadGesture(self.motion_service)
        self.arm_ges = ArmGesture(self.motion_service)
        self.hip_ges = HipGesture(self.motion_service)
        self.pep_move = PepperMove(self.motion_service)
        self.pep_expr = PepperExpression(0xffffff, self.conn.get_led_service())
        self.comp_handler = CompositeHandler(self.arm_ges, self.head_ges, self.pep_speech, self.pep_expr, self.hip_ges)
        self.connecting = False
    
    def __print(self, text):
        # type: (str) -> None
        print(self.program_id, text)

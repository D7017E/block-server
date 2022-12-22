"""
Code runner module which handles the code execution of programs
"""
import threading
import time
import re
from datetime import datetime
from handle_code.pepper_connection import PepperConnection # pylint: disable=unused-import
from handle_code.queue import Program # pylint: disable=unused-import
from behaviors import HipGesture, PepperExpression, HeadGesture, ArmGesture
from behaviors import PepperMove, PepperSpeech, CompositeHandler, PepperController, RPSController, WebController # pylint: disable=line-too-long

class ConnectionError(Exception):
    """
    Error class for connection errors
    """
    pass

class ExecInterrupt(Exception):
    """
    Interrupt class for exec
    """
    pass

# pylint: disable=too-many-instance-attributes
class CodeRunner(object):
    """
    Object for handling programs sent from blockly site
    """
    def __init__(
            self,
            program,
            timeout_program,
            conn,
            ip_address,
            password,
            api_key,
            search_key
        ): # pylint: disable=too-many-arguments
        # type: (Program, int, PepperConnection, str, str, str, str) -> CodeRunner
        self.program = program
        self.program_code = self.__process_program(program.get_program())
        self.timeout_program = timeout_program
        self.conn = conn
        self.should_exit = False
        self.connecting = False
        self.program_exited = False

        self.animated_speech_service = None
        self.motion_service = None
        self.auto_service = None
        self.behavior_service = None
        self.blinking_service = None
        self.speech_recognition_service = None
        self.tts_service = None
        self.led_service = None
        self.tablet_service = None

        self.pep_speech = None
        self.head_ges = None
        self.arm_ges = None
        self.hip_ges = None
        self.pep_move = None
        self.pep_expr = None
        self.comp_handler = None
        self.pep_controller = None
        self.rps_controller = None
        self.web_controller = None

        self.ip_address = ip_address
        self.password = password

        self.api_key = api_key
        self.search_key = search_key

    # pylint: disable=no-self-use
    def __process_program(self, program):
        # type: (str) -> str
        """
        Will add code between the program to be able to exit anywhere.
        Will replace every #AAaaAA color to 0xAAaaAA.
        Returns the program as a string.
        """
        def replace(match):
            """
            Returns 0x + the color
            """
            return "0x" + (match.group(1))[0:]

        _hex_colour = re.compile(r'#([0-9a-fA-F]{6})\b')
        program = self.__add_should_exit(program)
        return _hex_colour.sub(replace, program)

    def __add_should_exit(self, program):
        # type: (str) -> str
        """
        Returns the program but with an if statement between every line with a raise condition
        to be able to exit the program in the middle of execution.
        """
        new_program = ""
        for line in program.splitlines():
            spaces = len(line) - len(line.lstrip())
            spaces_str = " " * spaces
            new_program += spaces_str + "if self.should_exit:\n"
            new_program += spaces_str + "    raise ExecInterrupt\n"
            new_program += line + "\n"
        return new_program

    def start_execute_program(self):
        """
        Connects to Pepper and executes a program. Resets Pepper at the end.
        """
        self.__connect_to_pepper_timer(10)
        self.__reset_pepper(False)
        self.__execute_program()
        self.__reset_pepper(True)
        time.sleep(2)

    def __execute_program(self):
        self.should_exit = False
        threading.Thread(target=self.__exec).start()
        for _ in range(self.timeout_program):
            time.sleep(1)
            if self.program_exited:
                return
        self.should_exit = True
        time.sleep(3)
        if self.program_exited:
            return
        self.__reset_pepper(True)
        raise StopIteration("Force quit Pepper execution")

    def __exec(self):
        # pylint: disable=unused-variable
        self.__print("Running the program")
        pep_speech = self.pep_speech
        head_ges = self.head_ges
        arm_ges = self.arm_ges
        hip_ges = self.hip_ges
        pep_move = self.pep_move
        pep_expr = self.pep_expr
        comp_handler = self.comp_handler
        pep_controller = self.pep_controller
        rps_controller = self.rps_controller
        web_controller = self.web_controller
        try:
            exec(self.program_code) # pylint: disable=exec-used
        except ExecInterrupt:
            pass
        except Exception as exc: # pylint: disable=broad-except
            self.__print("Execution error: " + str(exc))
            self.program_exited = True
            return
        time.sleep(1)
        self.__print("Stopping the program")
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

    def __reset_pepper(self, interactive_mode):
        self.__print("Resetting Pepper")
        self.head_ges.reset_head()
        self.arm_ges.reset_arms()
        self.hip_ges.reset_hip()
        self.pep_move.stop_movement()
        self.pep_controller.reset()
        if interactive_mode:
            self.auto_service.setState("interactive")
        else:
            self.auto_service.setState("safeguard")
        time.sleep(0.5)
        self.__print("Done with resetting Pepper")

    def __configure_and_connect_to_pepper(self):
        """
        Configure a connection and services
        """
        self.__print("Trying to connect to Pepper")
        self.conn.connect()
        time.sleep(0.5)
        self.animated_speech_service = self.conn.get_animated_speech_service()
        self.motion_service = self.conn.get_motion_service()
        self.auto_service = self.conn.get_autonomous_service()
        self.behavior_service = self.conn.get_behavior_service()
        self.blinking_service = self.conn.get_blinking_service()
        self.speech_recognition_service = self.conn.get_speech_recognition_service()
        self.tts_service = self.conn.get_text_to_speech_service()
        self.led_service = self.conn.get_led_service()
        self.tablet_service = self.conn.get_tablet_service()

        self.motion_service.setIdlePostureEnabled("Head", False)
        self.auto_service.stopAll()
        self.behavior_service.stopAllBehaviors()
        self.blinking_service.setEnabled(False)

        self.pep_speech = PepperSpeech(self.animated_speech_service)
        self.head_ges = HeadGesture(self.motion_service)
        self.arm_ges = ArmGesture(self.motion_service)
        self.hip_ges = HipGesture(self.motion_service)
        self.pep_move = PepperMove(self.motion_service)
        self.pep_expr = PepperExpression(0xffffff, self.led_service)
        self.comp_handler = CompositeHandler(
            self.arm_ges, self.head_ges, self.pep_speech, self.pep_expr, self.hip_ges
        )
        self.pep_controller = PepperController(
            self.speech_recognition_service.getLanguage(),
            self.speech_recognition_service, self.tts_service
        )
        self.rps_controller = RPSController(
            self.ip_address,
            self.password
        )
        self.web_controller = WebController(
            self.animated_speech_service,
            self.tablet_service,
            self.speech_recognition_service,
            self.api_key,
            self.search_key
        )
        self.connecting = False

    def __print(self, text):
        # type: (str) -> None
        message = (
            str(datetime.now().strftime('%H:%M:%S.%f')[:-4]) + " - " + str(self.program.get_pid()) +
            " - " + text)
        if self.program.get_name() != "":
            message += " - Name: " + self.program.get_name()
        print("> " + message)

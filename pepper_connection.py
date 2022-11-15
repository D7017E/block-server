"""
The module handles a connection to pepper and also works as a service factory
"""
import qi
# pylint: disable=superfluous-parens

class PepperConnection(object):
    """
    This class handles a connection to Pepper and will also return a service from the connection
    """

    def __init__(self, _ip, port, user_name, password):
        self._ip = _ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.session = qi.Session()


    def connect(self):
        """
        Will connect to the Pepper robot
        """
        self.session.connect("tcp://{0}:{1}".format(self._ip, self.port))
        if self.session.isConnected():
            print("Successfully connected to robot")
        else:
            print("Error connecting to robot")
            raise ConnectionError("Error connecting to robot") # pylint: disable=undefined-variable

        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.load_system_host_keys()
        # ssh.connect(hostname=self.ip, username=self.user_name, password=self.password)

    def get_speech_service(self):
        """
        Returns a speech service from the connection
        """
        return self.session.service("ALAnimatedSpeech")

    def get_motion_service(self):
        """
        Returns a motion service from the connection
        """
        return self.session.service("ALMotion")

    def get_autonomous_service(self):
        """
        Returns a autonomous service from the connection
        """
        return self.session.service("ALAutonomousLife")

    def get_battery_service(self):
        """
        Returns a battery service from the connection
        """
        return self.session.service("ALBattery")

    def get_tablet_service(self):
        """
        Returns a tablet service from the connection
        """
        return self.session.service("ALTabletService")

    def get_led_service(self):
        """
        Returns a LED service from the connection
        """
        return self.session.service("ALLeds")

    def get_audio_service(self):
        """
        Returns a audio service from the connection
        """
        return self.session.service("ALAudioDevice")

    def get_behavior_service(self):
        """
        Returns a behavior service from the connection
        """
        return self.session.service("ALBehaviorManager")

    def get_blinking_service(self):
        """
        Returns a blinking service from the connection
        """
        return self.session.service("ALAutonomousBlinking")

    def get_sound_localization_service(self):
        """
        Returns a sound service from the connection
        """
        return self.session.service("ALSoundLocalization")

    def get_memory_service(self):
        """
        Returns a memory service from the connection
        """
        return self.session.service("ALMemory")

    def get_audio_player_service(self):
        """
        Returns a service for playing .wav files
        """
        return self.session.service("ALAudioPlayer")

import qi
import paramiko

class PepperConnection():

    def __init__(self, ip, port, user_name, password):
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.session = qi.Session()


    def connect(self):
        self.session.connect("tcp://{0}:{1}".format(self.ip, self.port))

        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.load_system_host_keys()
        # ssh.connect(hostname=self.ip, username=self.user_name, password=self.password)

    def get_speech_service(self):
        return self.session.service("ALAnimatedSpeech")

    def get_move_service(self):
        return self.session.service("ALMotion")

    def get_autonomous_service(self):
        return self.session.service("ALAutonomousLife")

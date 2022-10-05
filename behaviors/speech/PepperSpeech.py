

class PepperSpeech():
    
    def __init__(self, service):
        self.service = service
    
    def talk(self, text):
        self.service.say(("\\RSPD={0}\\ \\VCT={1} \\" + str(text)).format(100, 100))
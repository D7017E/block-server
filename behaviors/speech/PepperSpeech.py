

class PepperSpeech():
    
    def talk(self, service, text):
        service.say(("\\RSPD={0}\\ \\VCT={1} \\" + str(text)).format(100, 100))
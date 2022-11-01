"""
Class for making Pepper talk.
"""

# pylint: disable=too-few-public-methods

class PepperSpeech():
    """
    Class for making Pepper talk.
    """

    def __init__(self, service):
        """
        * <service>, an animated speech service
        Initializes the PepperSpeech object.
        """
        self.service = service

    def talk(self, text):
        """
        * <text> string of text for pepper to say
        Basic speech to text
        """
        self.service.say(("\\RSPD={0}\\ \\VCT={1} \\" + str(text)).format(100, 100))

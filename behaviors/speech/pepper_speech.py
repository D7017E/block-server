"""
Class for making Pepper talk.
"""

# pylint: disable=too-few-public-methods

class PepperSpeech(object):
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
        # type: (PepperSpeech, str) -> None
        """
        * <text> str, string of text for pepper to say
        Basic speech-to-text
        """
        self.service.say(str(text))

    def talk_without_gesture(self, text):
        # type: (PepperSpeech, str) -> None
        """
        * <text> str, string of text for pepper to say
        Speech-to-text without Pepper gesturing
        """
        self.service.say(
            ("\\RSPD={0}\\ \\VCT={1} \\" + str(text)).format(100, 100),
            {"bodyLanguageMode":"disabled"}
            )
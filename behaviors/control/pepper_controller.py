"""
This module handles controlling basic Pepper functionality.
"""

class PepperController(object):
    """
    Class for controlling basic Pepper functionality
    """

    def __init__(self, original_language, speech_recognition_service, tts_service):
        self.original_language = original_language
        self.speech_rec = speech_recognition_service
        self.tts = tts_service

    def change_language(self, language):
        # type: (PepperController, str) -> None
        """
        * <language> str, the language to set Pepper to

        Sets the language of the Pepper robot
        """

        self.speech_rec.pause(True)
        self.speech_rec.setLanguage(language)
        self.tts.setLanguage(language)
        self.speech_rec.pause(False)

    def set_volume(self, volume):
        # type: (PepperController, int) -> None
        """
        * <volume> int, the volume to set Pepper to

        Sets Pepper's volume
        """
        if volume <= 20 or volume > 100:
            print("Volume must be between 20 and 100")
            return
        volume = float(volume) / 100
        self.tts.setVolume(volume)

    def reset(self):
        # type: (PepperController) -> None
        """
        Resets Pepper's volume and language
        """
        self.tts.setVolume(1.0)
        self.change_language(self.original_language)
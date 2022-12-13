# -*- coding: utf-8 -*-

"""
Module for interacting with the web (Google, Wikipedia)
"""

import time
from ask_pepperonit import Ask

class WebController(object):
    """
    Class for interacting with the web (Google, Wikipedia)
    """

    def __init__(
            self,
            speech_service,
            tablet_service,
            speech_recognition_service,
            api_key="",
            search_key=""
        ): # pylint: disable=too-many-arguments
        """
        Initalize the class for interacting with the web (Google, Wikipedia)
        """
        self.ask = Ask(api_key, search_key)
        self.speech_service = speech_service
        self.tablet_service = tablet_service
        self.speech_recognition_service = speech_recognition_service

    def ask_google(self, text):
        # type: (WebController, str) -> None
        """
        Asks google a question and processes the result to display an image on Pepper's tablet.
        """
        if self.speech_recognition_service.getLanguage() == "English":
            self.say_question_en(text)
        elif self.speech_recognition_service.getLanguage() == "Swedish":
            self.say_question_sv(text)
        image = self.ask.ask_google_api(text)
        self.tablet_service.showImage(image)
        self._stop_showing()

    def ask_wikipedia(self, text):
        # type: (WebController, str) -> None
        """
        Asks Wikipedia a question and processes the result to have Pepper say the answer
        and display an image on Pepper's tablet.
        """
        lang = ""
        if self.speech_recognition_service.getLanguage() == "English":
            lang = "en"
            self.say_question_en(text)
        elif self.speech_recognition_service.getLanguage() == "Swedish":
            lang = "sv"
            self.say_question_sv(text)
        self.ask.wikipedia_set_lang(lang)
        text, image = self.ask.ask_wikipedia_api(text)
        self.tablet_service.showImage(image)
        if lang == "en":
            self.say_answer_en(text)
        elif lang == "sv":
            self.say_answer_sv(text)
        self._stop_showing()

    def say_question_en(self, question):
        # type: (WebController, str) -> None
        """
        Repeats a question in English.
        """
        self.speech_service.say(("I got the question \\RSPD={0}\\ \\VCT={1} \\"
                                 + question.encode('utf-8')).format(100, 100)
                               )
    def say_question_sv(self, question):
        # type: (WebController, str) -> None
        """
        Repeats a question in Swedish.
        """
        self.speech_service.say(("Jag fick frågan\\RSPD={0}\\ \\VCT={1} \\"
                                 + question.encode('utf-8')).format(100, 100)
                               )

    def say_answer_en(self, answer):
        # type: (WebController, str) -> None
        """
        Says the answer to a question in English.
        """
        self.speech_service.say(("My answer is \\RSPD={0}\\ \\VCT={1} \\"
                                 + answer.encode('utf-8')).format(100, 100)
                               )
    def say_answer_sv(self, answer):
        # type: (WebController, str) -> None
        """
        Says the answer to a question in Swedish.
        """
        self.speech_service.say(("Mitt svar är \\RSPD={0}\\ \\VCT={1} \\"
                                 + answer.encode('utf-8')).format(100, 100)
                               )

    def _stop_showing(self):
        time.sleep(5)
        self.tablet_service.hideImage()
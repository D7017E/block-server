"""
Module responsible for controlling rock-paper-scissors
"""

from prps import server_connection

class RPSController(object):
    """
    Class responsible for controlling rock-paper-scissors
    """

    def __init__(self, ip_address, password):
        self.ip_address = ip_address
        self.password = password

    def play_rps(self, language="Swedish"):
        # type: (RPSController, str) -> bool
        """
        Class for starting a game of rock-paper-scissors
        """
        server_connection.main(self.ip_address, self.password, language)

"""custom errors for the tic_tac_toe game"""

class GameEndError(Exception):
    def __init__(self, value):
        self.value = value

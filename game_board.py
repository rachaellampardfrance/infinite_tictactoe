"""create game board and logic"""

class GameBoard:

    players = ['X', 'O']

    def __init__(self, player):
        # initialise empty game board
        self.list = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]   
        self.player = player
        if self.player == 'X':
            self.bot = 'O'
        else:
            self.bot = 'X'

    def __str__(self):
        div_top = " ___________ "
        div_mid = "|---|---|---|"
        div_bottom = f" {chr(8254)*11} "
        # create board print loop
        board = f"""
        Player: {self.player}
        Computer: {self.bot}
        {div_top}
        | {self.list[0][0]} | {self.list[0][1]} | {self.list[0][2]} |
        {div_mid}
        | {self.list[1][0]} | {self.list[1][1]} | {self.list[1][2]} |
        {div_mid}
        | {self.list[2][0]} | {self.list[2][1]} | {self.list[2][2]} |
        {div_bottom}
        """
        return board    

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if not player in GameBoard.players:
            raise ValueError("Not a player") 
        self._player = player

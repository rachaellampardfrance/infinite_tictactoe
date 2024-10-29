"""create game board and logic"""

class GameBoard:

    player_tokens = ['X', 'O']
    board_index = [1, 2, 3]

    def __init__(self, player_token):
        # initialise empty game board
        self.list = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]   
        self.player_token = player_token
        if self.player_token == 'X':
            self.bot_token = 'O'
        else:
            self.bot_token = 'X'

    def __str__(self):
        div_top = " ___________ "
        div_mid = "|---|---|---|"
        div_bottom = f" {chr(8254)*11} "
        # create board print loop
        board = f"""
        Player: {self.player_token}
        Computer: {self.bot_token}
        {div_top}
        | {self.list[0][0]} | {self.list[0][1]} | {self.list[0][2]} |
        {div_mid}
        | {self.list[1][0]} | {self.list[1][1]} | {self.list[1][2]} |
        {div_mid}
        | {self.list[2][0]} | {self.list[2][1]} | {self.list[2][2]} |
        {div_bottom}
        """
        return board    
    
    def is_valid_placement(self, row, column):
        if row.isdigit() and column.isdigit():
            if self.is_board_location(row, column):
                if self.list[int(row) - 1][int(column) - 1] == ' ':
                    return True
                else:
                    return False
            else:
                raise ValueError("Not a valid location")
        else:
            raise ValueError("One or more inputs is not valid")
        
    @classmethod
    def is_board_location(cls, row, column):
        if row.isdigit() and column.isdigit():
            if int(row) in cls.board_index and int(column) in cls.board_index:
                return True
            return False
        else:
            raise ValueError("One or more inputs is not valid")
        

    @property
    def player_token(self):
        return self._player_token
    @player_token.setter
    def player_token(self, player_token):
        if not player_token in GameBoard.player_tokens:
            raise ValueError("Not a player") 
        self._player_token = player_token

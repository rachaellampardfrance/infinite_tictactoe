"""create game board and logic"""

class GameBoard:

    player_tokens = ['X', 'O']

    def __init__(self, player_token, size=3):
        """initialise empty game board
        size default is 3"""
        self.size = size
        self.index = self.generate_index()
        self.list = self.generate_list()
        self.player_token = player_token
        self.bot_token = self.assign_bot_token()


    def __str__(self):
        """return formatted string of players
        and game board instance in it's current state"""

        # generate board top, dividers and bottom
        # by game board instance size
        top = " "
        divide = "|"
        bottom = " "
        for i in range(self.size):
            divide += "---|"
            if not i == self.size - 1:
                top += "____"
                bottom += f"{chr(8254)*4}"
            else:
                # one shorter with space
                top += "___ "
                bottom += f"{chr(8254)*3} "

        # Generate game board with loop for 
        # allocating item placements in rows
        board = (f"Player: {self.player_token}\n"
        f"Computer: {self.bot_token}\n"
        f"{top}")
        for i in range(self.size):
            board += "\n|"
            for j in range(self.size):
                board += f" {self.list[i][j]} |"
            if not i == self.size - 1:
                board += f"\n{divide}"
            else:
                board += f"\n{bottom}"
        return board
    

    def generate_index(self):
        index = []
        for i in range(self.size):
            index.append(i + 1) 
        return index


    def generate_list(self):
        table = []  
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(' ')
            table.append(row)       
        return table
    

    def assign_bot_token(self):
        if self.player_token == 'X':
            return 'O'
        elif self.player_token == 'O':
            return 'X'
        raise ValueError("Error assigning 'bot_token', 'self.player_token' not equal to 'X' or 'O'")
        

    
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
        

    def is_board_location(self, row, column):
        if row.isdigit() and column.isdigit():
            if int(row) in self.index and int(column) in self.index:
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

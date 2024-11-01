"""create game board and logic"""
from validation import validate_str, validate_digit

class GameBoard:

    PLAYER_TOKENS = ['X', 'O']
    DEFAULT_LIST_ITEM = ' '

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
        if not self.is_board_location(row, column):
             raise ValueError("Not a valid location")
        
        item = self.get_list_item(row, column)

        if self.is_default_list_item(item):
            return True
        return False

    def get_list_item(self, row, column):
        validate_str(row, column)
        if not (row.isdigit() and column.isdigit()):
            raise ValueError("One or more inputs is not valid")
        
        return self.list[int(row) - 1][int(column) - 1]
                    
    def is_board_location(self, row, column):
        if row.isdigit() and column.isdigit():
            if int(row) in self.index and int(column) in self.index:
                return True
            return False
        else:
            raise ValueError("One or more inputs is not valid")
        
    @classmethod
    def is_default_list_item(cls, item):
        validate_str(item)
        return item == cls.DEFAULT_LIST_ITEM
    
    @property
    def player_token(self):
        return self._player_token
    @player_token.setter
    def player_token(self, player_token):
        if not player_token in GameBoard.PLAYER_TOKENS:
            raise ValueError("Not a player") 
        self._player_token = player_token

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if type(size) == int:
            if 3 <= size <= 5:
                self._size = size
            else:
                raise ValueError("argument 'size' must be between 3 - 5 inclusive")
        else:
            raise ValueError("'size' must be of type 'int'")
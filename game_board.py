"""create game board and logic"""
from validation import validate_str, validate_digit, validate_int

class GameBoard:

    PLAYER_TOKENS = ['X', 'O']
    DEFAULT_LIST_ITEM = ' '
    MIN_SIZE = 3
    MAX_SIZE = 5

    def __init__(self, player_token, size=MIN_SIZE):
        """initialise empty game board
        size default is 3"""
        self.size = size
        self.index = self.generate_index()
        self.list = self.generate_list()
        self.player_token = player_token
        self.bot_token = self.get_bot_token()


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
    

    def get_bot_token(self):
        self.validate_user_token()

        if self.player_token == 'X':
            return 'O'
        return 'X'
    

    def validate_user_token(self):
        if self.player_token not in GameBoard.PLAYER_TOKENS:
            raise ValueError("Player token is not set to 'X' or 'O'")

    
    def is_valid_placement(self, row, column):
        self.validate_board_location(row, column)
        
        item = self.get_list_item(row, column)

        if self.is_default_list_item(item):
            return True
        return False


    def get_list_item(self, row, column):
        # validate_str(row, column)
        validate_digit(row, column)
        
        return self.list[int(row) - 1][int(column) - 1]


    def validate_board_location(self, row, column):
        validate_digit(row, column)
        
        if not (int(row) in self.index and int(column) in self.index):
            raise ValueError("Not a valid location")

        
    @classmethod
    def is_default_list_item(cls, item):
        validate_str(item)

        return item == cls.DEFAULT_LIST_ITEM
    

    @classmethod
    def validate_size(cls, size):
        if not cls.MIN_SIZE <= size <= cls.MAX_SIZE:
            raise ValueError("argument 'size' must be between 3 - 5 inclusive")
    

    @classmethod
    def valid_token(cls, token):
        if not token in cls.PLAYER_TOKENS:
            raise ValueError(f"{token} is not a valid player token. Valid tokens 'X', 'O'")


    @property
    def player_token(self):
        return self._player_token
    @player_token.setter
    def player_token(self, player_token):
        GameBoard.valid_token(player_token)
         
        self._player_token = player_token


    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        validate_int(size)
        GameBoard.validate_size(size)
        
        self._size = size

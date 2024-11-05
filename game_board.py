"""create game board and validation"""
from validation import validate_str, validate_digit, validate_int

class GameBoard:
    """create a game board with varied size
    
    class constants:
    DEFAULT_LIST_ITEM -- default char that fills board spaces
    MIN_SIZE -- minimum int size of size argument 
    MAX_SIZE -- maximum int size of size argument
    
    instance variables:
    size -- size of the board by (size * size) 
    index -- an array of ints from 1 to max size inclusive
    list -- a nested array of board locations set by size
    """

    DEFAULT_LIST_ITEM = ' '
    MIN_SIZE = 3
    MAX_SIZE = 5

    def __init__(self, size=MIN_SIZE):
        """initialise empty game board

        keyword arguments:
        size -- 'int' (default 3)
        """
        self.size = size
        self.index = self.generate_index()
        self.list = self.generate_list()


    def __str__(self):
        """return formatted string of players
        and game board instance in it's current state
        """

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
        board = f"{top}"
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
        """return array from 1 - size inclusive"""
        index = []
        for i in range(self.size):
            index.append(i + 1)
        return index


    def generate_list(self):
        """return nested array with length of size"""
        table = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(' ')
            table.append(row)
        return table


    def validate_placement(self, row, column):
        """raise errors location is taken"""
        item = self.get_list_item(row, column)

        if not self.is_default_list_item(item):
            raise ValueError("placement is already taken, try again")


    def get_list_item(self, row, column):
        """return item at specific board location"""
        self.validate_board_location(row, column)
        validate_digit(row, column)

        return self.list[int(row) - 1][int(column) - 1]


    def validate_board_location(self, row, column):
        """raise error if not a board location"""
        validate_digit(row, column)

        if not (int(row) in self.index and int(column) in self.index):
            raise ValueError("Not a board location")


    def min_max(self):
        """return min max"""
        return {"min": self.index[0], "max": self.index[-1]}


    @classmethod
    def is_default_list_item(cls, item):
        """return true/false"""
        validate_str(item)

        return item == cls.DEFAULT_LIST_ITEM


    @classmethod
    def validate_size(cls, size):
        """raise error if size not within min/max class consts"""
        if not cls.MIN_SIZE <= size <= cls.MAX_SIZE:
            raise ValueError("argument 'size' must be between 3 - 5 inclusive")


    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        """return size if valid"""
        validate_int(size)
        GameBoard.validate_size(size)

        self._size = size

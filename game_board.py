"""create game board and validation"""
from validation import validate_str, validate_int, validate_positive_int
from messages import error_message

class GameBoard:
    """create a game board with varied size
    
    class constants:
    DEFAULT_LIST_ITEM -- default char that fills board spaces
    MIN_SIZE -- minimum int size of size argument 
    MAX_SIZE -- maximum int size of size argument

    instance variables:
    size -- size of the board by (size * size) 
    list -- a nested array of board locations set by size
    """

    DEFAULT_LIST_ITEM = ' '
    BOX_SIZE = 4
    MIN_SIZE = 3
    MAX_SIZE = 5

    def __init__(self, size=MIN_SIZE, box_size=BOX_SIZE):
        """initialise empty game board

        keyword arguments:
        size -- 'int' (default GameBoard.MIN_SIZE)
        box_size -- 'int' (default GameBoard.BOX_SIZE) 
        """
        self.size = size
        self.list = self._generate_list()
        self.box = box_size


    def __str__(self):
        """return formatted string of players
        and game board instance in it's current state
        """
    
        top = self._format_board_top()
        divide = self._format_board_divide()
        bottom = self._format_board_bottom()
        board = self._format_board(top, divide, bottom)
        return board

    def _format_board_top(self):
        """format top of board by size"""
        top = " "
        for i in range(self.size):
            if i == self.size - 1:
                top += f"{' ':_>{self.box}}"
            else:
                top += f"{'':_^{self.box}}"
        return top

    def _format_board_divide(self):
        """format board divide by size"""
        divide = "|"
        for _ in range(self.size):
            divide += f"{'|':->{self.box}}"
        return divide

    def _format_board_bottom(self):
        """format bottom of board by size"""
        bottom = " "
        for i in range(self.size):
            if i == self.size - 1:
                # one shorter with space
                bottom += f"{' ':{chr(8254)}>{self.box}} "
            else:
                bottom += f"{'':{chr(8254)}>{self.box}}"
        return bottom

    def _format_board(self, top, divide, bottom):
        """format board by size
        
        keyvalue arguments:
        top -- formatted string (create with self.format_board_top())
        divide -- formatted string (create with self.format_board_divide())
        bottom -- formatted string (create with self.format_board_bottom())
        """
        board = top
        for i in range(self.size):
            board += "\n|"
            for j in range(self.size):
                board += f"{self.list[i][j]:^{self.box - 1}}" + "|"
            if not i == self.size - 1:
                board += f"\n{divide}"
            else:
                board += f"\n{bottom}"
        return board


    def _generate_list(self):
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
            raise ValueError(error_message("6"))


    def get_list_item(self, row, column):
        """return item at specific board location"""
        self.validate_board_location(row, column)

        return self.list[row][column]


    def validate_board_location(self, row, column):
        """raise error if not a board location"""
        validate_int(row, column)

        if not (row in range(self.size) and column in range(self.size)):
            raise ValueError(error_message("7"))


    @classmethod
    def is_default_list_item(cls, item):
        """return true/false"""
        validate_str(item)

        return item == cls.DEFAULT_LIST_ITEM


    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        """return size if valid"""
        validate_int(size)
        GameBoard.validate_size(size)

        self._size = size

    @classmethod
    def validate_size(cls, size):
        """raise error if size not within min/max class const"""
        if not cls.MIN_SIZE <= size <= cls.MAX_SIZE:
            raise ValueError(error_message("8", cls.MIN_SIZE, cls.MAX_SIZE))


    @property
    def box(self):
        return self._box
    @box.setter
    def box(self, box_size):
        """return size if valid"""
        validate_positive_int(box_size)

        self._box = box_size

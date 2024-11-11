"""create game board and validation"""
from helpers.validation import validate_str, validate_int, validate_positive_int
from helpers.messages.messages import error_message, user_error_message

class GameBoard:
    """create a game board to valid size
    
    :DEFAULT_LIST_ITEM: const 'str' - default char to fill board spaces
    :BOX_SIZE: const 'int' - default box size
    :MIN_SIZE: const 'int' - minimum for size argument 
    :MAX_SIZE: const 'int' - maximum for size argument
    """

    DEFAULT_LIST_ITEM: str = ' '
    BOX_SIZE: int = 4
    MIN_SIZE: int = 3
    MAX_SIZE: int = 5

    def __init__(self, size: int=MIN_SIZE, box_size: int=BOX_SIZE):
        """initialise empty game board

        :param size: 'int' sets the size of the nested array for the board.

            (default GameBoard.MIN_SIZE). cannot exceed MAX_SIZE or be less than MIN_SIZE
        :param box_size: 'int' (default GameBoard.BOX_SIZE)
            must be positive
        """
        self.size: int = size
        self.list: list = self._generate_list()
        self.box: int = box_size


    def __str__(self) -> str:
        """return formatted string of players
        and game board instance in it's current state
        """
    
        top: str = self._format_board_top()
        divide: str = self._format_board_divide()
        bottom: str = self._format_board_bottom()
        board: str = self._format_board(top, divide, bottom)
        return board

    def _format_board_top(self) -> str:
        """format top of board by self.size"""
        top: str = " "
        for i in range(self.size):
            if i == self.size - 1:
                top += f"{' ':_>{self.box}}"
            else:
                top += f"{'':_^{self.box}}"
        return top

    def _format_board_divide(self) -> str:
        """format board divide by self.size"""
        divide: str = "|"
        for _ in range(self.size):
            divide += f"{'|':->{self.box}}"
        return divide

    def _format_board_bottom(self) -> str:
        """format bottom of board by self.size"""
        bottom: str = " "
        for i in range(self.size):
            if i == self.size - 1:
                # allows for last iteration to allow a whitespace
                bottom += f"{' ':{chr(8254)}>{self.box}}"
            else:
                bottom += f"{'':{chr(8254)}>{self.box}}"
        return bottom

    def _format_board(self, top: str, divide: str, bottom: str) -> str:
        """format board by size
        
        :param top: formatted 'str' from - self.format_board_top()
        :param divide: formatted 'str' from - self.format_board_divide()
        :param bottom: formatted 'str' from - self.format_board_bottom()
        :returns: formatted 'str' of current GameBoard object with tokens
        """
        board: str = top
        for i in range(self.size):
            board += "\n|"
            for j in range(self.size):
                board += f"{self.list[i][j]:^{self.box - 1}}" + "|"
            if not i == self.size - 1:
                board += f"\n{divide}"
            else:
                board += f"\n{bottom}"
        return board


    def _generate_list(self) -> list:
        """:returns: nested 'list' for the BoardGame instance object"""
        table: list = []
        for _ in range(self.size):
            row: list = []
            for _ in range(self.size):
                row.append(' ')
            table.append(row)
        return table


    def validate_placement(self, row: int, column: int) -> None:
        """raise error if location is taken"""
        item: str = self.get_list_item(row, column)

        if not self.is_default_list_item(item):
            raise ValueError(user_error_message("2"))


    def get_list_item(self, row: int, column: int) -> str:
        """:returns: 'str' of the object at the nested list location"""
        self.validate_board_location(row, column)

        return self.list[row][column]


    def validate_board_location(self, row: int, column: int) -> None:
        """raise error if not a board location"""
        validate_int(row, column)

        if not (row in range(self.size) and column in range(self.size)):
            raise ValueError(user_error_message("3"))


    @classmethod
    def is_default_list_item(cls, item: str) -> bool:
        """return true/false"""
        validate_str(item)

        return item == cls.DEFAULT_LIST_ITEM


    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size: int) -> None:
        """set self._size to 'int' size if valid"""
        validate_int(size)
        GameBoard.validate_size(size)

        self._size = size

    @classmethod
    def validate_size(cls, size: int) -> None:
        """raise error if size not within min/max class const"""
        if not cls.MIN_SIZE <= size <= cls.MAX_SIZE:
            raise ValueError(error_message("5", cls.MIN_SIZE, cls.MAX_SIZE))


    @property
    def box(self) -> int:
        return self._box
    @box.setter
    def box(self, box_size: int) -> None:
        """set self._box to 'int' box_size if valid"""
        validate_positive_int(box_size)

        self._box = box_size

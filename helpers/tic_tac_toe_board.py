"""TicTacToeBoard class"""
from helpers.messages.messages import user_error_message
from helpers.game_board import GameBoard
from helpers.custom_errors import GameEndError
from helpers.computer import TicTacToeComputer

class TicTacToeBoard(GameBoard, TicTacToeComputer):
    """creates an instance of a 'tic tac toe' game

    :GameBoard: parent class that init's the "board"

    :TicTacToeComputer: parent class that holds functions
    for the computer player logic for 'tic tac toe'
    """

    MIN_SIZE: int = 3
    # set format size for board boxes
    BOX_SIZE: int = 4


    def __init__(self, size: int=MIN_SIZE, box_size: int=BOX_SIZE):
        """initialise board instance using GameBoard parent"""
        GameBoard.__init__(self, size = size, box_size = box_size)

    def validate_game_on(self) -> None:
        """bubbles winner or stalemate GameEndError"""
        self._check_for_winner()
        self._check_for_stalemate()

    def _check_for_winner(self) -> None:
        """bubble GameEndError if winner found"""
        self._check_rows_columns()
        self._check_top_right_diagonal()
        self._check_bottom_right_diagonal()

    def _check_rows_columns(self) -> None:
        """bubble GameEndError if winner found"""
        for i in range(self.size):
            self._check_row_column( i)

    def _check_row_column(self, itr: int) -> None:
        """raises GameEndError if any row or column is all the same token
        
        :param board: A GameBoard object
        :param itr: 'int' for iteration
        """
        row_icons: set = set()
        column__icons: set = set()

        for i in range(self.size):
            row_icons.add(self.list[itr][i])
            column__icons.add(self.list[i][itr])
        if len(row_icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in row_icons:
            raise GameEndError(user_error_message("4", row_icons.pop()))
        if len(column__icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in column__icons:
            raise GameEndError(user_error_message("4", column__icons.pop()))

    def _check_top_right_diagonal(self) -> None:
        """raises GameEndError if top right down diagonal is all the same token"""
        icons: set = set()
        for i in range(self.size):
            icons.add(self.list[i][i])
        if len(icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in icons:
            raise GameEndError(user_error_message("4", icons.pop()))

    def _check_bottom_right_diagonal(self) -> None:
        """raises GameEndError if bottom right up diagonal is all the same token"""
        icons: set = set()
        size: int = self.size - 1
        for i in range(self.size):
            icons.add(self.list[i][size - i])
        if len(icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in icons:
            raise GameEndError(user_error_message("4", icons.pop()))


    def _check_for_stalemate(self) -> None:
        """raises GameEndError no default GameBoard list item
            is found in board
        """
        table: list = self.list

        for i in range(self.size):
            for j in range(self.size):
                if table[i][j] == GameBoard.DEFAULT_LIST_ITEM:
                    return

        raise GameEndError(user_error_message("5"))

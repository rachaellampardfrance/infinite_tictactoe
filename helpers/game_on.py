"""helper functions for tic_tac_toe to check if there was a winner
functions raise GameEndError with related strings"""
from helpers.messages.messages import user_error_message
from helpers.game_board import GameBoard 
from helpers.custom_errors import GameEndError

def validate_game_on(board: object) -> None:
    """bubbles winner or stalemate GameEndError"""
    _check_for_winner(board)
    _check_for_stalemate(board)


def _check_for_winner(board: object) -> None:
    """bubble GameEndError if winner found"""
    _check_rows_columns(board)
    _check_top_right_diagonal(board)
    _check_bottom_right_diagonal(board)

def _check_rows_columns(board: object) -> None:
    """bubble GameEndError if winner found"""
    for i in range(board.size):
        _check_row_column(board, i)

def _check_row_column(board: object, itr: int) -> None:
    """raises GameEndError if any row or column is all the same token
    
    :param board: A GameBoard object
    :param itr: 'int' for iteration
    """
    row_icons: set = set()
    column__icons: set = set()

    for i in range(board.size):
        row_icons.add(board.list[itr][i])
        column__icons.add(board.list[i][itr])
    if len(row_icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in row_icons:
        raise GameEndError(user_error_message("4", row_icons.pop()))
    if len(column__icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in column__icons:
        raise GameEndError(user_error_message("4", column__icons.pop()))

def _check_top_right_diagonal(board: object) -> None:
    """raises GameEndError if top right down diagonal is all the same token"""
    icons: set = set()
    for i in range(board.size):
        icons.add(board.list[i][i])
    if len(icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in icons:
        raise GameEndError(user_error_message("4", icons.pop()))

def _check_bottom_right_diagonal(board: object) -> None:
    """raises GameEndError if bottom right up diagonal is all the same token"""
    icons: set = set()
    size: int = board.size - 1
    for i in range(board.size):
        icons.add(board.list[i][size - i])
    if len(icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in icons:
        raise GameEndError(user_error_message("4", icons.pop()))


def _check_for_stalemate(board: object) -> None:
    """raises GameEndError no default GameBoard list item
        is found in board
    """
    table: list = board.list

    for i in range(board.size):
        for j in range(board.size):
            if table[i][j] == GameBoard.DEFAULT_LIST_ITEM:
                return

    raise GameEndError(user_error_message("5"))
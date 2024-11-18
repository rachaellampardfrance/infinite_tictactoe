# from helpers.game_board import GameBoard
from helpers.tic_tac_toe_board import TicTacToeBoard
from helpers.messages.messages import user_error_message
from helpers.custom_errors import GameEndError
import pytest

def test_check_for_winner_3x3():
    """check win conditions"""

     # diagonal wins
    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # Top to bottom diagonal: X win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', ' ', 'O'],
            [' ', 'X', ' '],
            ['O', ' ', 'X']
        ]
        assert game_board.validate_game_on()

    with pytest.raises(GameEndError, match=user_error_message("4", "O")):
        # Top to bottom diagonal:  O win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['O', 'X', 'X'],
            ['X', 'O', ' '],
            [' ', ' ', 'O']
        ]
        assert game_board.validate_game_on()
    
    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # Bottom to top diagonal: X win
        game_board = TicTacToeBoard()
        game_board.list = [
            [' ', 'O', 'X'],
            [' ', 'X', 'O'],
            ['X', ' ', 'O']
        ]
        assert game_board.validate_game_on()

    # row wins
    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # X win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', 'X', 'X'],
            [' ', ' ', 'O'],
            ['O', ' ', 'O']
        ]
        assert game_board.validate_game_on()
    
    with pytest.raises(GameEndError, match=user_error_message("4", "O")):
        # O win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', ' ', 'X'],
            [' ', 'X', 'O'],
            ['O', 'O', 'O']
        ]
        assert game_board.validate_game_on()

    # colum wins
    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # X win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', ' ', 'X'],
            [' ', 'O', 'X'],
            ['O', 'O', 'X']
        ]
        assert game_board.validate_game_on()

    with pytest.raises(GameEndError, match=user_error_message("4", "O")):
        # O win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', 'O', ' '],
            [' ', 'O', 'X'],
            ['O', 'O', 'X']
        ]
        assert game_board.validate_game_on()

    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # O win
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', 'O', 'O'],
            ['X', ' ', ' '],
            ['X', 'O', ' ']
        ]
        assert game_board.validate_game_on()

def test_stalemate_3x3():
    """GameEndError raises with stalemate message"""
    with pytest.raises(GameEndError, match=user_error_message("5")):
        game_board = TicTacToeBoard()
        game_board.list = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O']
        ]
        assert game_board.validate_game_on()


def test_check_for_winner_10x10():
    """check max board size"""

    # diagonal wins
    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # Top to bottom diagonal: X win
        game_board = TicTacToeBoard(size=10)
        game_board.list = [
            ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']
        ]
        assert game_board.validate_game_on()

    with pytest.raises(GameEndError, match=user_error_message("4", "X")):
        # Top to bottom diagonal: X win
        game_board = TicTacToeBoard(size=10)
        game_board.list = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        assert game_board.validate_game_on()

    # row wins
    with pytest.raises(GameEndError, match=user_error_message("4", "O")):
        # Top to bottom diagonal: X win
        game_board = TicTacToeBoard(size=10)
        game_board.list = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        assert game_board.validate_game_on()

    # columns wins
    with pytest.raises(GameEndError, match=user_error_message("4", "O")):
        # Top to bottom diagonal: X win
        game_board = TicTacToeBoard(size=10)
        game_board.list = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O']
        ]
        assert game_board.validate_game_on()

def test_stalemate_10x10():
    """check max board size"""

    with pytest.raises(GameEndError, match=user_error_message("5")):
        # Top to bottom diagonal: X win
        game_board = TicTacToeBoard(size=10)
        game_board.list = [
            ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
            ['O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'],
            ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X'],
            ['O', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O'],
            ['X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
            ['O', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'O'],
            ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X'],
            ['O', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']
        ]
        assert game_board.validate_game_on()
        
from helpers.tic_tac_toe_board import TicTacToeBoard
from helpers.tokens import Tokens

def test_priority():
    # (computer is 'O')
    tokens = Tokens('X')

    # prioritise winning
    board = TicTacToeBoard()
    board.list = [
        [' ', ' ', ' '],
        ['X', ' ', 'O'],
        ['X', ' ', 'O']
    ]
    assert board.get_hard_choice(tokens) == {"row": 0, "column": 2}
    
    # prioritise blocking player
    board.list = [
        ['X', ' ', 'O'],
        [' ', 'X', ' '],
        [' ', 'O', ' ']
    ]
    assert board.get_hard_choice(tokens) == {"row": 2, "column": 2}

    # prioritise best progression
    board = TicTacToeBoard()
    board.list = [
        ['X', 'O', ' '],
        ['O', ' ', ' '],
        ['X', 'X', 'O']
    ]
    assert board.get_hard_choice(tokens) == {"row": 1, "column": 1}

    # prioritise blocking player
    board = TicTacToeBoard()
    board.list = [
        [' ', ' ', 'X'],
        ['X', ' ', 'O'],
        ['O', ' ', 'X']
    ]
    assert board.get_hard_choice(tokens) == {"row": 0, "column": 0}


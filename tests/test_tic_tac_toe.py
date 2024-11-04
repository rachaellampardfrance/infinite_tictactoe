from game_board import GameBoard
from tic_tac_toe import check_for_winner

def test_check_for_winner():
    """check win conditions"""
    game_board = GameBoard()
    
    # diagonal wins
    # left to right: X win
    game_board.list = [
        ['X', ' ', 'O'],
        [' ', 'X', ' '],
        ['O', ' ', 'X']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : X"
    # left to right:  O win
    game_board.list = [
        ['O', 'X', 'X'],
        ['X', 'O', ' '],
        [' ', ' ', 'O']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : O"
    # right to left: X win
    game_board.list = [
        [' ', 'O', 'X'],
        [' ', 'X', 'O'],
        ['X', ' ', 'O']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : X"

    # row wins
    # X win
    game_board.list = [
        ['X', 'X', 'X'],
        [' ', ' ', 'O'],
        ['O', ' ', 'O']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : X"
    # O win
    game_board.list = [
        ['X', ' ', 'X'],
        [' ', 'X', 'O'],
        ['O', 'O', 'O']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : O"

    # colum wins
    # X win
    game_board.list = [
        [' ', ' ', 'X'],
        [' ', 'O', 'X'],
        ['O', 'O', 'X']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : X"
    # O win
    game_board.list = [
        ['X', 'O', ' '],
        [' ', 'O', 'X'],
        ['O', 'O', 'X']
    ]
    assert check_for_winner(game_board.list) == "WINNER! : O"
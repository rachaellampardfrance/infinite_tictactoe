from game_board import GameBoard
import pytest

def test_init():
    # correct board initialisation
    game_board = GameBoard('X')
    assert game_board.list == [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    # correct player and bot markers
    game_board = GameBoard('X')
    assert game_board.player_token == 'X' and game_board.bot_token == 'O'
    game_board = GameBoard('O')
    assert game_board.player_token == 'O' and game_board.bot_token == 'X'
    # raises errors with invalid player type
    with pytest.raises(ValueError, match="Not a player"):
        game_board = GameBoard('1')
    with pytest.raises(ValueError, match="Not a player"):
        game_board = GameBoard('a')
    with pytest.raises(ValueError, match="Not a player"):
        game_board = GameBoard('!')

def test_is_board_location():
    # check class method identifies all board locations
    assert GameBoard.is_board_location('1', '3') == True
    assert GameBoard.is_board_location('3', '1') == True
    assert GameBoard.is_board_location('0', '1') == False
    assert GameBoard.is_board_location('4', '3') == False
    assert GameBoard.is_board_location('1', '0') == False
    assert GameBoard.is_board_location('3', '4') == False

def test_valid_placement():
    # confirms valid placement
    game_board = GameBoard('X')
    assert game_board.is_valid_placement('1', '1') == True

    # raises error if placement is not a board location
    with pytest.raises(ValueError, match="Not a valid location"):
        game_board = GameBoard('X')
        game_board.is_valid_placement('0', '1')
    with pytest.raises(ValueError, match="Not a valid location"):
        game_board = GameBoard('X')
        game_board.is_valid_placement('1', '4')

    # False if location occupied
    game_board = GameBoard('X')
    game_board.list = [     
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert game_board.is_valid_placement('1', '1') == False

    # raises error if passed in placements are not digits
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board = GameBoard('O')
        game_board.is_valid_placement('a', '1')

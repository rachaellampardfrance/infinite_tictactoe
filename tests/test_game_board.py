from game_board import GameBoard
import pytest

def test_init():
    """test GameBoard initialisation"""
    # correct board list generated on initial
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
    """check function can identify all board locations"""
    # identifies board locations and non existent locations
    assert GameBoard.is_board_location('1', '3') == True
    assert GameBoard.is_board_location('3', '1') == True
    assert GameBoard.is_board_location('0', '1') == False
    assert GameBoard.is_board_location('4', '3') == False
    assert GameBoard.is_board_location('1', '0') == False
    assert GameBoard.is_board_location('3', '4') == False

    # raises error if either input value is not a digit
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        GameBoard.is_board_location('a', '1')
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        GameBoard.is_board_location('!', '1')
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        GameBoard.is_board_location('1', 'a')
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        GameBoard.is_board_location('1', '!')


def test_valid_placement():
    # confirms valid placement
    game_board = GameBoard('X')
    assert game_board.is_valid_placement('1', '1') == True

    # False if location occupied
    game_board = GameBoard('X')
    game_board.list = [     
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert game_board.is_valid_placement('1', '1') == False

    # raises error if placement is not a board location
    with pytest.raises(ValueError, match="Not a valid location"):
        game_board = GameBoard('X')
        game_board.is_valid_placement('0', '1')
    with pytest.raises(ValueError, match="Not a valid location"):
        game_board = GameBoard('X')
        game_board.is_valid_placement('1', '4')

    # raises error if passed in placements are not digits
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board = GameBoard('O')
        game_board.is_valid_placement('a', '1')

def test_str():
    """test printing the 'game board'
    player tokens and pieces from self.list"""

    # from initial
    game_board = GameBoard('X')
    assert game_board.__str__() == """
        Player: X
        Computer: O
         ___________ 
        |   |   |   |
        |---|---|---|
        |   |   |   |
        |---|---|---|
        |   |   |   |
         ‾‾‾‾‾‾‾‾‾‾‾ 
        """
    
    # from ongoing game
    game_board = GameBoard('O')
    game_board.list = [     
        ['X', ' ', 'O'],
        [' ', 'O', 'X'],
        [' ', ' ', ' ']
    ]
    assert game_board.__str__() == """
        Player: O
        Computer: X
         ___________ 
        | X |   | O |
        |---|---|---|
        |   | O | X |
        |---|---|---|
        |   |   |   |
         ‾‾‾‾‾‾‾‾‾‾‾ 
        """
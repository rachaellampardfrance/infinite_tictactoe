from helpers.game_board import GameBoard
from helpers.messages.messages import error_message, user_error_message
import pytest

def test_init():
    """test GameBoard initialisation"""
    # correct board list generated on initial
    game_board = GameBoard()
    assert (game_board.size == 3
            and game_board.list == [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']
        ])

    # test setting size value to none default sets
    #  size, index and list correctly
    game_board = GameBoard(size=10)
    assert (game_board.size == 10 
            and game_board.list == [
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])


def test_size():
    """size of board is set correctly"""

    # default size
    game_board = GameBoard()
    assert game_board.size == GameBoard.MIN_SIZE
    # argument sizes
    game_board = GameBoard(GameBoard.MIN_SIZE)
    assert game_board.size == GameBoard.MIN_SIZE
    game_board = GameBoard(5)
    assert game_board.size == 5
    game_board = GameBoard(GameBoard.MAX_SIZE)
    assert game_board.size == GameBoard.MAX_SIZE

    # size only accepts 3-10 range inclusive
    with pytest.raises(
        ValueError,
        match=error_message(
            "1",
            GameBoard.MIN_SIZE,
            GameBoard.MAX_SIZE
        )):
        game_board = GameBoard(GameBoard.MIN_SIZE - 1)

    with pytest.raises(
        ValueError,
        match=error_message(
            "1",
            GameBoard.MIN_SIZE,
            GameBoard.MAX_SIZE
        )):
        game_board = GameBoard(-1)

    with pytest.raises(
        ValueError,
        match=error_message(
            "1",
            GameBoard.MIN_SIZE,
            GameBoard.MAX_SIZE
        )):
        game_board = GameBoard(GameBoard.MAX_SIZE + 1)


    # size only accepts 'int' type
    checks = [[], {}, "", ()]
    for check in checks:
        with pytest.raises(TypeError):
            game_board = GameBoard(check)


def test_validate_board_location():
    """check function can identify all board locations"""

    # minimum board size
    # does not raise error: valid board location
    game_board = GameBoard()
    try:
        game_board.validate_board_location(0, GameBoard.MIN_SIZE - 1)
    except:
        assert False, "validate_board_location(0, 2) raised an exception"
    # raises error: out of bounds board locations 
    with pytest.raises(ValueError, match=user_error_message("3")):
        game_board.validate_board_location(-1, 0)
    with pytest.raises(ValueError, match=user_error_message("3")):
        game_board.validate_board_location(0, GameBoard.MIN_SIZE)


    # maximum board size
    # does not raise error: valid board location
    game_board = GameBoard(size=GameBoard.MAX_SIZE)
    try:
        game_board.validate_board_location(0, GameBoard.MAX_SIZE - 1)
    except:
        assert False, "validate_board_location(0, 9) raised an exception"
    # raises error: out of bounds board locations 
    with pytest.raises(ValueError, match=user_error_message("3")):
        game_board.validate_board_location(-1, 0)
    with pytest.raises(ValueError, match=user_error_message("3")):
        game_board.validate_board_location(0, GameBoard.MAX_SIZE)



def test_validate_placement():
    """raises ValueError if placement is already taken"""

    # smallest size board 
    # valid placement at max location
    game_board = GameBoard()
    try:
        game_board.validate_placement(GameBoard.MIN_SIZE - 1, GameBoard.MIN_SIZE - 1)
    except:
        assert False, "validate_placement(GameBoard.MIN_SIZE - 1, GameBoard.MIN_SIZE - 1) raised an error"
    # now already taken
    game_board.list[GameBoard.MIN_SIZE - 1][GameBoard.MIN_SIZE - 1] = 'X'
    with pytest.raises(ValueError, match=user_error_message("2")):
        game_board.validate_placement(GameBoard.MIN_SIZE - 1, GameBoard.MIN_SIZE - 1) 

    # largest size board
    # valid placement at max location
    game_board = GameBoard(size=GameBoard.MAX_SIZE)
    try:
        game_board.validate_placement(GameBoard.MAX_SIZE - 1, GameBoard.MAX_SIZE - 1)
    except:
        assert False, "validate_placement(GameBoard.MAX_SIZE - 1, GameBoard.MAX_SIZE - 1) raised an error"
    # now already taken
    game_board.list[GameBoard.MAX_SIZE - 1][GameBoard.MAX_SIZE - 1] = 'X'
    with pytest.raises(ValueError, match=user_error_message("2")):
        game_board.validate_placement(GameBoard.MAX_SIZE - 1, GameBoard.MAX_SIZE - 1)


def test_get_list_item():
    game_board = GameBoard()
    game_board.list = [     
        ['X', ' ', ' '],
        [' ', 'O', ' '],
        [' ', ' ', 'X']
    ]
    assert game_board.get_list_item(0, 0) == 'X'
    assert game_board.get_list_item(1, 1) == 'O'
    assert game_board.get_list_item(2, 2) == 'X'
    assert game_board.get_list_item(2, 1) == ' '


def test_str():
    """test printing the 'game board'
    player tokens and pieces from self.list"""

    # from initial
    game_board = GameBoard()
    assert game_board.__str__() == (
        " ___________ \n"
        "|   |   |   |\n"
        "|---|---|---|\n"
        "|   |   |   |\n"
        "|---|---|---|\n"
        "|   |   |   |\n"
        " ‾‾‾‾‾‾‾‾‾‾‾ ")
    
    # from ongoing game
    game_board = GameBoard()
    game_board.list = [     
        ['X', ' ', 'O'],
        [' ', 'O', 'X'],
        [' ', ' ', ' ']
    ]
    assert game_board.__str__() == (
        " ___________ "
        "\n| X |   | O |"
        "\n|---|---|---|"
        "\n|   | O | X |"
        "\n|---|---|---|"
        "\n|   |   |   |"
        "\n ‾‾‾‾‾‾‾‾‾‾‾ ")
    

def test_str_large():
    """Test boards larger than default size"""
    # from initial
    game_board = GameBoard(size=4)
    assert game_board.__str__() == (
        " _______________ \n"
        "|   |   |   |   |\n"
        "|---|---|---|---|\n"
        "|   |   |   |   |\n"
        "|---|---|---|---|\n"
        "|   |   |   |   |\n"
        "|---|---|---|---|\n"
        "|   |   |   |   |\n"
        " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
    
    # from ongoing game
    game_board = GameBoard(size=5)
    game_board.list = [     
        ['X', ' ', 'O', ' ', ' '],
        [' ', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O']
    ]
    assert game_board.__str__() == (
        " ___________________ \n"
        "| X |   | O |   |   |\n"
        "|---|---|---|---|---|\n"
        "|   | O |   |   |   |\n"
        "|---|---|---|---|---|\n"
        "|   |   |   | X |   |\n"
        "|---|---|---|---|---|\n"
        "|   |   | X |   |   |\n"
        "|---|---|---|---|---|\n"
        "|   |   |   |   | O |\n"
        " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
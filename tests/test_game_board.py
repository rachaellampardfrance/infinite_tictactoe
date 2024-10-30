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
    # correct player and bot tokens set
    game_board = GameBoard('X')
    assert game_board.player_token == 'X' and game_board.bot_token == 'O'
    game_board = GameBoard('O')
    assert game_board.player_token == 'O' and game_board.bot_token == 'X'

    # test setting size value to none default sets
    #  size, index and list correctly
    game_board = GameBoard('X', 5)
    assert game_board.size == 5 and game_board.index == [1, 2, 3, 4, 5] and game_board.list == [     
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            ]


def test_size():
    """size of board is set correctly"""

    # default size
    game_board = GameBoard('X')
    assert game_board.size == 3
    # argument sizes
    game_board = GameBoard('X', 3)
    assert game_board.size == 3
    game_board = GameBoard('X', 4)
    assert game_board.size == 4
    game_board = GameBoard('X', 5)
    assert game_board.size == 5    

    # size only accepts 3-5 range inclusive
    with pytest.raises(ValueError, match="argument 'size' must be between 3 - 5 inclusive"):
        game_board = GameBoard('X', 1)
    with pytest.raises(ValueError, match="argument 'size' must be between 3 - 5 inclusive"):
        game_board = GameBoard('X', -1)
    with pytest.raises(ValueError, match="argument 'size' must be between 3 - 5 inclusive"):
        game_board = GameBoard('X', 6)

    # size only accepts 'int' type
    with pytest.raises(ValueError, match="'size' must be of type 'int'"):
        game_board = GameBoard('X', 'a')
    with pytest.raises(ValueError, match="'size' must be of type 'int'"):
        game_board = GameBoard('X', '!')


def test_generate_index():
    """index list is generated correctly on init"""
    game_board = GameBoard('X', 5)
    assert game_board.generate_index() == [1, 2, 3, 4, 5] 
    game_board = GameBoard('X', 4)
    assert game_board.generate_index() == [1, 2, 3, 4] 


def test_generate_list():
    game_board = GameBoard('X')
    assert game_board.list == [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
    game_board = GameBoard('X', 5)
    assert game_board.list == [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']]
    

def test_player_token():
    """player token sets token == the argument"""
    # correct player token assigned 
    game_board = GameBoard('X')
    assert game_board.player_token == 'X'
    game_board = GameBoard('O')
    assert game_board.player_token == 'O'

    # raises errors: invalid player token
    with pytest.raises(ValueError, match="Not a player"):
        game_board = GameBoard('1')
    with pytest.raises(ValueError, match="Not a player"):
        game_board = GameBoard('a')
    with pytest.raises(ValueError, match="Not a player"):
        game_board = GameBoard('!')


def test_assign_bot_token():
    """should assign opposite token from player"""

    # correct bot token assignment
    game_board = GameBoard('X')
    assert game_board.bot_token == 'O'
    game_board = GameBoard('O')
    assert game_board.bot_token == 'X'


def test_is_board_location():
    """check function can identify all board locations"""

    # True: identifies existing board locations
    game_board = GameBoard('X')
    assert game_board.is_board_location('1', '3') == True
    assert game_board.is_board_location('3', '1') == True
    # False: locations are not existing board locations
    assert game_board.is_board_location('0', '1') == False
    assert game_board.is_board_location('4', '3') == False
    assert game_board.is_board_location('1', '0') == False
    assert game_board.is_board_location('3', '4') == False
    # raises error: either input value is not a digit
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board.is_board_location('a', '1')
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board.is_board_location('!', '1')
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board.is_board_location('1', 'a')
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board.is_board_location('1', '!')


def test_is_valid_placement():
    """returns True if the location is unoccupied
    and False if occupied"""

    # True: valid placement
    game_board = GameBoard('X')
    assert game_board.is_valid_placement('1', '1') == True

    # False: occupied location
    game_board = GameBoard('X')
    game_board.list = [     
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert game_board.is_valid_placement('1', '1') == False

    # raises error: placement is not a board location
    with pytest.raises(ValueError, match="Not a valid location"):
        game_board = GameBoard('X')
        game_board.is_valid_placement('0', '1')
    with pytest.raises(ValueError, match="Not a valid location"):
        game_board = GameBoard('X')
        game_board.is_valid_placement('1', '4')

    # raises error: passed in placements are not digits
    with pytest.raises(ValueError, match="One or more inputs is not valid"):
        game_board = GameBoard('O')
        game_board.is_valid_placement('a', '1')


def test_str():
    """test printing the 'game board'
    player tokens and pieces from self.list"""

    # from initial
    game_board = GameBoard('X')
    assert game_board.__str__() == (
        "Player: X\n"
        "Computer: O\n"
        " ___________ \n"
        "|   |   |   |\n"
        "|---|---|---|\n"
        "|   |   |   |\n"
        "|---|---|---|\n"
        "|   |   |   |\n"
        " ‾‾‾‾‾‾‾‾‾‾‾ ")
    
    # from ongoing game
    game_board = GameBoard('O')
    game_board.list = [     
        ['X', ' ', 'O'],
        [' ', 'O', 'X'],
        [' ', ' ', ' ']
    ]
    assert game_board.__str__() == (
        "Player: O\n"
        "Computer: X\n"
        " ___________ \n"
        "| X |   | O |\n"
        "|---|---|---|\n"
        "|   | O | X |\n"
        "|---|---|---|\n"
        "|   |   |   |\n"
        " ‾‾‾‾‾‾‾‾‾‾‾ ")
    

def test_str_large():
    """Test boards larger than default size"""
    # from initial
    game_board = GameBoard('X', 4)
    assert game_board.__str__() == (
        "Player: X\n"
        "Computer: O\n"
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
    game_board = GameBoard('X', 5)
    game_board.list = [     
        ['X', ' ', 'O', ' ', ' '],
        [' ', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O']
    ]
    assert game_board.__str__() == (
        "Player: X\n"
        "Computer: O\n"
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
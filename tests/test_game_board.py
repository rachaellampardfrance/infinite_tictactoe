from helpers.game_board import GameBoard
import pytest

def test_init():
    """test GameBoard initialisation"""
    # correct board list generated on initial
    game_board = GameBoard()
    assert game_board.list == [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    # test setting size value to none default sets
    #  size, index and list correctly
    game_board = GameBoard(5)
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
    game_board = GameBoard()
    assert game_board.size == 3
    # argument sizes
    game_board = GameBoard(3)
    assert game_board.size == 3
    game_board = GameBoard(4)
    assert game_board.size == 4
    game_board = GameBoard(5)
    assert game_board.size == 5    

    # size only accepts 3-5 range inclusive
    with pytest.raises(ValueError, match="argument 'size' must be between 3 - 5 inclusive"):
        game_board = GameBoard(1)
    with pytest.raises(ValueError, match="argument 'size' must be between 3 - 5 inclusive"):
        game_board = GameBoard(-1)
    with pytest.raises(ValueError, match="argument 'size' must be between 3 - 5 inclusive"):
        game_board = GameBoard(6)

    # size only accepts 'int' type
    with pytest.raises(ValueError, match="'str' is not of type 'int'"):
        game_board = GameBoard('a')
    with pytest.raises(ValueError, match="'dict' is not of type 'int'"):
        game_board = GameBoard({})
    with pytest.raises(ValueError, match="'list' is not of type 'int'"):
        game_board = GameBoard([1, 2])
    with pytest.raises(ValueError, match="'tuple' is not of type 'int'"):
        game_board = GameBoard(())


def test_generate_index():
    """index list is generated correctly on init"""
    game_board = GameBoard(5)
    assert game_board.generate_index() == [1, 2, 3, 4, 5] 
    game_board = GameBoard(4)
    assert game_board.generate_index() == [1, 2, 3, 4] 
    game_board = GameBoard(3)
    assert game_board.generate_index() == [1, 2, 3] 


def test_generate_list():
    game_board = GameBoard()
    assert game_board.list == [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
    game_board = GameBoard(5)
    assert game_board.list == [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']]


def test_validate_board_location():
    """check function can identify all board locations"""

    # does not raise error: valid board location 
    game_board = GameBoard()
    try:
        game_board.validate_board_location('1', '3')
    except:
        assert False, "'1', '3' raised an exception"
    # raises error: out of bounds board locations 
    with pytest.raises(ValueError, match="Not a board location"):
        game_board.validate_board_location('0', '1')
    with pytest.raises(ValueError, match="Not a board location"):
        game_board.validate_board_location('1', '4')
    # raises error: either input value is not a digit
    with pytest.raises(ValueError, match="'a' is not a digit"):
        game_board.validate_board_location('a', '1')
    with pytest.raises(ValueError, match="'!' is not a digit"):
        game_board.validate_board_location('!', '1')
    with pytest.raises(ValueError, match="'a' is not a digit"):
        game_board.validate_board_location('1', 'a')
    with pytest.raises(ValueError, match="'!' is not a digit"):
        game_board.validate_board_location('1', '!')
    # raises error: either input value is not of type 'str'
    with pytest.raises(ValueError, match="'int' is not of type 'str'"):
        game_board.validate_board_location(1, '1')
    with pytest.raises(ValueError, match="'list' is not of type 'str'"):
        game_board.validate_board_location([1, 2], '1')


def test_validate_placement():
    """returns True if the location is unoccupied
    and False if occupied"""

    # True: valid placement
    game_board = GameBoard()
    try:
        game_board.validate_placement('1', '1')
    except:
        assert False, "'1', '1' raised an error"

    # False: occupied location
    game_board = GameBoard()
    game_board.list = [     
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    with pytest.raises(ValueError, match="placement is already taken, try again"):
        game_board.validate_placement('1', '1') 

    # raises error: placement is not a board location
    with pytest.raises(ValueError, match="Not a board location"):
        game_board.validate_placement('0', '1')
    with pytest.raises(ValueError, match="Not a board location"):
        game_board.validate_placement('1', '4')

    # raises error: passed in placements are not digits
    with pytest.raises(ValueError, match="'a' is not a digit"):
        game_board.validate_placement('a', '1')


def test_get_list_item():
    game_board = GameBoard()
    game_board.list = [     
        ['X', ' ', ' '],
        [' ', 'O', ' '],
        [' ', ' ', 'X']
    ]
    assert game_board.get_list_item('1', '1') == 'X'
    assert game_board.get_list_item('2', '2') == 'O'
    assert game_board.get_list_item('3', '3') == 'X'
    assert game_board.get_list_item('3', '2') == ' '

    with pytest.raises(ValueError, match="'a' is not a digit"):
        game_board.get_list_item('a', '1')
    with pytest.raises(ValueError, match="'list' is not of type 'str'"):
        game_board.get_list_item([1, 2, 3], '1')
    with pytest.raises(ValueError, match="'int' is not of type 'str'"):
        game_board.get_list_item(1, '1')



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
    game_board = GameBoard(4)
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
    game_board = GameBoard(5)
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
"""This program runs a game of tic tac toe"""
from random import randint
from helpers.custom_errors import GameEndError
from helpers.tic_tac_toe_board import TicTacToeBoard
from helpers.messages.messages import user_error_message, user_message
from helpers.tokens import Tokens
from helpers.validation import validate_digit, item_exists


# for values displayed to the user
DISPLAY_MIN_RANGE: int = 1
DISPLAY_MAX_RANGE: int = 0
# for real values for indexing TicTacToeBoard arrays
MIN_RANGE: int = 0
MAX_RANGE: int = 0


def main() -> None:
    try:
        """tic tac toe game creation and game loop"""
        game_board, player_tokens = init_game()
        print_game(game_board, player_tokens)

        # game loop
        game_loop(game_board, player_tokens)
    except KeyboardInterrupt:
        print("")
    finally:
        exit_message()


def init_game() -> tuple:
    """:returns: tuple of TicTacToeBoard and Tokens objects"""
    board: object = create_game_board()
    set_max_ranges(board)
    tokens: object = set_tokens()
    return board, tokens


def create_game_board() -> object:
    """:returns: new TicTacToeBoard object"""
    game_board: object = TicTacToeBoard()
    return game_board


def set_max_ranges(board: object) -> None:
    """set global ranges by TicTacToeBoard object instance size"""
    global MAX_RANGE, DISPLAY_MAX_RANGE

    MAX_RANGE = board.size - 1
    DISPLAY_MAX_RANGE = board.size


def set_tokens() -> object:
    """:returns: Token object with assigned player tokens"""
    created: bool = False
    while created is False:
        try:
            player_tokens: object = Tokens(get_player1_token_choice())
            created = True

        except ValueError as e:
            show_message(e)

    return player_tokens


def get_player1_token_choice() -> str:
    """get user token choice from available tokens
    
    :returns: 'str' of user token choice"""
    tokens: object = Tokens.PLAYER_TOKENS
    return input(user_message("1", tokens[0], tokens[1])).strip().upper()



def print_game(board: object, tokens: object) -> None:
    """print player tokens and TicTacToeBoard objects"""
    print(tokens)
    print(board)


def game_loop(board: object, tokens: object) -> None:
    """loop turns, printing board, 
    win and stalemate checks, and game on choice"""
    try:
        game_on: bool = True
        while game_on:
            board = user_placement(board, tokens)
            print_game(board, tokens)
            board.validate_game_on()
            board = bot_turn(board, tokens)
            print_game(board, tokens)
            board.validate_game_on()
            game_on = game_on_choice()

    except GameEndError as e:
        game_end_error_message(e)
        return None


def user_placement(board: object, tokens: object) -> object:
    """get user placement choice and try place
    
    :param board: TicTacToeBoard object
    :param tokens: Token object
    :returns: the TicTacToeBoard object with placed token"""
    while True:
        try:
            choice: dict = get_user_row_column()

        except ValueError as e:
            show_message(e)

        else:
            choice: dict = convert_user_input(choice)

            try:
                return try_place(board, choice, tokens.player1_token)
            
            except ValueError as e:
                show_message(e)


def get_user_row_column() -> dict:
    """get user row and column placement choice
    
    :returns: dict with 'row', 'column' keys and 'str' values"""
    row: str = input(user_message("2", DISPLAY_MIN_RANGE, DISPLAY_MAX_RANGE)).strip()
    validate_user_choice_input(row)

    column: str = input(user_message("3", DISPLAY_MIN_RANGE, DISPLAY_MAX_RANGE)).strip()
    validate_user_choice_input(column)
 
    choice = {
        "row": row,
        "column": column
    }
    return choice


def validate_user_choice_input(item):
    validate_digit(item)
    item_exists(item)


def convert_user_input(choice: dict) -> dict:
    """convert user choices from str to int
    
    :returns: dict with 'row', 'column' keys and 'int' values"""
    choice["row"] = int(choice["row"]) - 1
    choice["column"] = int(choice["column"]) - 1
    return choice


def try_place(board: object, location: dict, token: str) -> object:
    """try to place token at location 

    :param board: A TicTacToeBoard object
    :param location: A dict containing 
        {"row": int, "column": int} key variables
    :param token: Must be in Token.PLAYER_TOKENS
    :returns: The input TicTacToeBoard object with placed token
    """
    row: int = location["row"]
    column: int = location["column"]
    board.validate_placement(row, column)
    board.list[row][column] = token
    return board


def bot_turn(board: object, tokens: object) -> object:
    """computer token placement
    
    :returns: the TicTacToeBoard object with computers token placement"""
    while True:
        choice: dict = get_easy_bot_choice()
        try:
            return try_place(board, choice, tokens.player2_token)
        except ValueError:
            pass


def get_easy_bot_choice() -> dict:
    """generate random choice row/column from global ranges
    
    :returns: dict with 'row', 'column' keys and 'int' values"""
    row: int = randint(MIN_RANGE, MAX_RANGE)
    column: int = randint(MIN_RANGE, MAX_RANGE)
    return {"row": row, "column": column}


def game_on_choice() -> bool:
    """check if user wants to continue playing
    
    :returns: True if users wishes to continue, False if not"""
    while True:
        choice: str = input(user_message("4")).strip().upper()
        try:
            validate_game_on_choice(choice)
            if choice == "Y":
                return True
            return False

        except ValueError as e:
            show_message(e)


def validate_game_on_choice(choice: str) -> None:
    """raise error if choice is not valid"""
    valid: list = ['Y', 'N']
    if not choice in valid:
        raise ValueError(user_message("5", choice))


def show_message(e: str) -> None:
    print(e)

def game_end_error_message(e: str) -> None:
    print(user_error_message("6", e))

def exit_message() -> None:
    print(user_message("6"))


if __name__ == '__main__':
    main()

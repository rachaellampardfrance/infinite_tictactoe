"""This program runs a game of tic tac toe"""
from helpers.custom_errors import GameEndError
from helpers.messages.messages import (
    user_message,
    show_message,
    game_end_error_message,
    exit_message)
from helpers.tic_tac_toe_board import TicTacToeBoard
from helpers.tokens import Tokens
from helpers.validation import validate_digit

from pyfiglet import Figlet


# for values displayed to the user
DISPLAY_MIN_RANGE: int = 1
DISPLAY_MAX_RANGE: int = 0
# for real values for indexing TicTacToeBoard arrays
MIN_RANGE: int = 0
MAX_RANGE: int = 0


def main() -> None:
    """tic tac toe game creation and game loop"""
    print_logo()

    try:
        players = get_players()
        board_size = get_board_size()
        difficulty = get_difficulty(players)
        game_board, player_tokens = init_tictactoe_game(players, board_size)
        print_game(game_board, player_tokens)

        # game loop
        game_loop(game_board, player_tokens, players, difficulty)
    except KeyboardInterrupt:
        print("")
    finally:
        exit_message()

def print_logo():
    f = Figlet(font='standard', width=100)

    print(f.renderText("Infinite Tic Tac Toe"))


def get_players() -> int:
    options = ['2P', 'C']

    while True:
        choice = input(user_message("7")).strip().upper()

        if choice == options[0]:
            return 2
        elif choice == options[1]:
            return 1


def get_board_size():
    min_size = TicTacToeBoard.MIN_SIZE
    max_size = TicTacToeBoard.MAX_SIZE

    while True:
        size = input(user_message("8", min_size, max_size)).strip()
        try:
            validate_digit(size)
        except:
            continue
        else:
            if min_size <= int(size) <= max_size:
                return int(size)


def init_tictactoe_game(players: int, board_size: int) -> tuple:
    """:returns: tuple of TicTacToeBoard and Tokens objects"""
    board: object = create_game_board(board_size)
    set_global_max_ranges(board)
    tokens: object = set_tokens(players)

    return board, tokens


def create_game_board(board_size: int) -> object:
    """:returns: new TicTacToeBoard object"""
    game_board: object = TicTacToeBoard(board_size)
    return game_board


def set_global_max_ranges(board: object) -> None:
    """set global ranges by TicTacToeBoard object instance size"""
    global MAX_RANGE, DISPLAY_MAX_RANGE

    MAX_RANGE = board.size - 1
    DISPLAY_MAX_RANGE = board.size


def set_tokens(players: int) -> object:
    """:returns: Token object with assigned player tokens"""
    while True:
        player1_token = get_player1_token_choice()

        try:
            if players == 2:
                player_tokens: object = Tokens(player1_token)
                
            else:
                player_tokens: object = Tokens(player1_token, 'Computer')

            return player_tokens

        except ValueError as e:
            show_message(e)


def get_difficulty(players: int) -> str | None:
    if players == 1:
        while True:
            difficulty = input("Choose difficulty easy/hard: ").strip().lower()
            if difficulty in ['e', 'easy']:
                return 'easy'
            elif difficulty in ['h', 'hard']:
                return 'hard'
    return None


def get_player1_token_choice() -> str:
    """get user token choice from available tokens
    
    :returns: 'str' of user token choice"""
    tokens: object = Tokens.PLAYER_TOKENS
    return input(user_message("1", tokens[0], tokens[1])).strip().upper()


def print_game(board: object, tokens: object) -> None:
    """print player tokens and TicTacToeBoard objects"""
    print(tokens)
    print(board)



def game_loop(board: object, tokens: object, players: int, difficulty: str) -> None:
    """loop turns, printing board, 
    win and stalemate checks, and game on choice"""
    try:
        game_on: bool = True
        while game_on:
            board = user_placement(board, tokens.player1_token, "Player 1:")
            print_game(board, tokens)
            board.validate_game_on()
            

            if players == 2:
                board = user_placement(board, tokens.player2_token, "Player 2:")
            else:
                board = computer_turn(board, tokens, difficulty)

            print_game(board, tokens)
            board.validate_game_on()
            game_on = game_on_choice()

    except GameEndError as e:
        game_end_error_message(e)
        return None


def user_placement(board: object, token: str, user: str) -> object:
    """get user placement choice and try place
    
    :param board: TicTacToeBoard object
    :param tokens: Token object
    :returns: the TicTacToeBoard object with placed token"""
    while True:
        try:
            choice: dict = get_user_row_column(user)

        except ValueError as e:
            show_message(e)

        else:
            choice: dict = convert_user_input(choice)

            try:
                return try_place(board, choice, token)
            
            except ValueError as e:
                show_message(e)


def get_user_row_column(user: str) -> dict:
    """get user row and column placement choice
    
    :returns: dict with 'row', 'column' keys and 'str' values"""
    row: str = input(user_message("2", user, DISPLAY_MIN_RANGE, DISPLAY_MAX_RANGE)).strip()
    validate_user_digit_input(row)

    column: str = input(user_message("3", user, DISPLAY_MIN_RANGE, DISPLAY_MAX_RANGE)).strip()
    validate_user_digit_input(column)

    return {"row": row, "column": column}


def validate_user_digit_input(item: str):
    """raises errors if item not digit or not exists"""
    validate_digit(item)


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


def computer_turn(board: object, tokens: object, difficulty: str = 'easy') -> object:
    """computer token placement
    
    :returns: the TicTacToeBoard object with computers token placement"""
    while True:
        if difficulty == 'easy':
            choice: dict = board.get_easy_choice()
        else:
            choice: dict = board.get_hard_choice(tokens)

        try:
            return try_place(board, choice, tokens.player2_token)
        except ValueError:
            # print(f"computer failed to place")
            pass


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


if __name__ == '__main__':
    main()
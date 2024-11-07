"""This program runs a game of tic tac toe"""
from random import randint
from helpers.custom_errors import GameEndError
from helpers.game_board import GameBoard
from helpers.messages.messages import error_message, user_message
from helpers.tokens import Tokens
from helpers.validation import validate_digit


# for values displayed to the user
DISPLAY_MIN_RANGE = 1
DISPLAY_MAX_RANGE = 0
# for real values for indexing GameBoard arrays
MIN_RANGE = 0
MAX_RANGE = 0


def main():
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


def init_game():
    """create game board and set player tokens"""
    board = create_game_board()
    set_max_ranges(board)
    tokens = set_tokens()
    return board, tokens


def create_game_board():
    """create GameBoard object"""
    created = False
    while created is False:
        try:
            game_board = GameBoard()
            created = True
        except ValueError as e:
            value_error_message(e)
        except TypeError as e:
            type_error_message(e)
    return game_board


def set_max_ranges(board):
    """set ranges by board size"""
    global MAX_RANGE, DISPLAY_MAX_RANGE

    MAX_RANGE = board.size - 1
    DISPLAY_MAX_RANGE = board.size


def set_tokens():
    """Create token object with associated player tokens"""
    created = False
    while created is False:
        try:
            player_tokens = Tokens(get_user_token_choice())
            created = True

        except ValueError as e:
            value_error_message(e)
        except TypeError as e:
            type_error_message(e)

    return player_tokens


def get_user_token_choice():
    tokens = Tokens.PLAYER_TOKENS
    return input(user_message("1", tokens[0], tokens[1])).strip().upper()



def print_game(board, tokens):
    """print player tokens and GameBoard objects"""
    print(tokens)
    print(board)


def game_loop(board, tokens):
    """loop turns, printing board, 
    win and stalemate checks, and game on choice
    """

    try:
        game_on = True
        while game_on:
            board = user_placement(board, tokens)
            print_game(board, tokens)
            validate_game_on(board)
            board = bot_turn(board, tokens)
            print_game(board, tokens)
            validate_game_on(board)
            game_on = game_on_choice()

    except GameEndError as e:
        game_end_error_message(e)
        return


def user_placement(board, tokens):
    """get user placement choice and try place"""
    while True:
        choice = get_user_row_column()
        try:
            validate_digit(choice["row"], choice["column"])
            choice = convert_user_input(choice)
            return try_place(board, choice, tokens.user_token)
        except ValueError as e:
            value_error_message(e)
        except TypeError as e:
            type_error_message(e)


def get_user_row_column():
    """get user row and column placement return dict"""
    row = input(user_message("2", DISPLAY_MIN_RANGE, DISPLAY_MAX_RANGE))
    column = input(user_message("3", DISPLAY_MIN_RANGE, DISPLAY_MAX_RANGE))
    choice = {
        "row": row,
        "column": column
    }
    return choice


def convert_user_input(choice):
    choice["row"] = int(choice["row"]) - 1
    choice["column"] = int(choice["column"]) - 1
    return choice


def try_place(board, location, token):
    """try to place token at location 

    keyword arguments:
    board -- a GameBoard object
    location -- a dict containing 
        {"row": a, "column": b} key variables
    token -- must be in Token.PLAYER_TOKENS
    """
    row = location["row"]
    column = location["column"]
    board.validate_placement(row, column)
    board.list[row][column] = token
    return board


def bot_turn(board, tokens):
    """bot placement"""
    while True:
        index_choice = get_easy_bot_choice()
        try:
            return try_place(board, index_choice, tokens.bot_token)
        except ValueError as e:
            value_error_message(error_message("10", e))
        except TypeError as e:
            type_error_message(error_message("10", e))


def get_easy_bot_choice():
    """generate random choice row/column from global ranges"""
    row = randint(MIN_RANGE, MAX_RANGE)
    column = randint(MIN_RANGE, MAX_RANGE)
    return {"row": row, "column": column}



def validate_game_on(board):
    """player turn"""
    winner = check_for_winner(board)
    if winner:
        raise GameEndError(error_message("11", winner))
    
    if is_stalemate(board):
        raise GameEndError(error_message("12"))


def check_for_winner(board):
    """Check for winner"""
    table = board.list
    winner = ''

    # check any row is all the same token
    for i in range(3):
        if (table[i][0] == table[i][1] == table[i][2]
            and not table[i][0] == ' '):
            winner = table[i][0]

    #  check any column is all the same token
    for i in range(3):
        if (table[0][i] == table[1][i] == table[2][i]
            and not table[0][i] == ' '):
            winner = table[0][i]

    #  check any diagonal is all the same token
    if (table[0][0] == table[1][1] == table[2][2]
        and not table[0][0] == ' '):
        winner = table[0][0]
    elif (table[0][2] == table[1][1] == table[2][0]
          and not table[1][1] == ' '):
        winner = table[1][1]

    if winner:
        return winner
    return None


def is_stalemate(board):
    """check if stalemate"""
    table = board.list

    for i in range(3):
        if table[i][0] == ' ' or table[i][1] == ' ' or table[i][2] == ' ':
            return False
    return True


def game_on_choice():
    """check if user wants to continue playing"""
    while True:
        choice = input(user_message("4")).upper()
        try:
            validate_game_on_choice(choice)
            if choice == "Y":
                return True
            return False

        except ValueError as e:
            value_error_message(e)


def validate_game_on_choice(choice):
    valid = ['Y', 'N']
    if not choice in valid:
        raise ValueError(user_message("5", choice))

def show_error_message(e):
    """format + show error message"""
    print(error_message("13", e))

def value_error_message(e):
    print(error_message("14", e))

def type_error_message(e):
    print(error_message("15", e))

def game_end_error_message(e):
    print(error_message("16", e))

def exit_message():
    print(user_message("6"))


if __name__ == '__main__':
    main()

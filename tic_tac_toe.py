"""This program runs a game of tic tac toe"""
from random import randint
from game_board import GameBoard
from tokens import Tokens
from validation import validate_digit


# for values displayed to the user
DISPLAY_MIN_RANGE = 1
DISPLAY_MAX_RANGE = 0
# for real values for indexing GameBoard arrays
MIN_RANGE = 0
MAX_RANGE = 0


def main():
    """tic tac toe game creation and game loop"""
    game_board, player_tokens = init_game()
    print_game(game_board, player_tokens)

    # game loop
    game_loop(game_board, player_tokens)


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
            show_error_message(e)
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
            player_token = input("Choose X or O: ").strip().upper()
            player_tokens = Tokens(player_token)
            created = True
        except ValueError as e:
            show_error_message(e)
    return player_tokens


def print_game(board, tokens):
    """print player tokens and GameBoard objects"""
    print(tokens)
    print(board)


def game_loop(board, tokens):
    """loop turns, printing board, 
    win and stalemate checks, and game on choice
    """
    game_on = True
    try:
        while game_on:
            board = user_placement(board, tokens)
            turn(board, tokens)
            board = bot_turn(board, tokens)
            turn(board, tokens)
            game_on = game_on_choice()
    except ValueError as win:
        show_win_message(win)


def user_placement(board, tokens):
    """get user placement choice and try place"""
    while True:
        try:
            choice = get_user_row_column()
            validate_digit(choice["row"], choice["row"])
            choice = convert_user_input(choice)
            return try_place(board, choice, tokens.user_token)
        except ValueError as e:
            show_error_message(e)


def get_user_row_column():
    """get user row and column placement return dict"""
    row = input(f"select row location {DISPLAY_MIN_RANGE}-{DISPLAY_MAX_RANGE}: ")
    column = input(f"select column location {DISPLAY_MIN_RANGE}-{DISPLAY_MAX_RANGE}: ")
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
    token -- token 'X' or 'O'
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
            show_error_message(f"Bot triggered Error: '{e}'")


def get_easy_bot_choice():
    """generate random choice row/column from global ranges"""
    row = randint(MIN_RANGE, MAX_RANGE)
    column = randint(MIN_RANGE, MAX_RANGE)
    return {"row": row, "column": column}



def turn(board, tokens):
    """player turn"""
    print_game(board, tokens)
    winner = check_for_winner(board)

    if winner:
        raise ValueError(winner)

    if is_stalemate(board):
        raise ValueError("Stalemate!")


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
    choice = 'none'
    yes_no = ['Y', 'N']

    while choice not in yes_no:

        choice = input("Continue playing Y/N? ").upper()
        if choice not in yes_no:
            print(f"{choice} is not a valid option, try again")

    if choice == "Y":
        return True
    return False


def show_error_message(e):
    """format + show error message"""
    print(f"ERROR: {e}")


def show_win_message(win):
    """format + show winner message"""
    print(f"WINNER! : {win}")


if __name__ == '__main__':
    main()

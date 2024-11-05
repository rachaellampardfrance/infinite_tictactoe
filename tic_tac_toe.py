"""This program runs a game of tic tac toe"""
from random import randint
from game_board import GameBoard
from tokens import Tokens


def main():
    """tic tac toe game creation and game loop"""
    game_board, player_tokens = init_game()
    print_game(game_board, player_tokens)

    # game loop
    game_loop(game_board, player_tokens)


def init_game():
    """create game board and set player tokens"""
    board = create_game_board()
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
        placement_choice = get_user_row_column(board)
        try:
            return try_place(board, placement_choice, tokens.user_token)
        except ValueError as e:
            show_error_message(e)


def get_user_row_column(board):
    """get user row and column placement 
    
    get Gameboard object min max size for user range string
    and get user input for return dict"""
    board_range = board.min_max()
    min_range = board_range["min"]
    max_range = board_range["max"]

    row = input(f"select row location {min_range}-{max_range}: ")
    column = input(f"select column location {min_range}-{max_range}: ")
    index = {
        "row": row,
        "column": column
    }
    return index


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
    board.list[int(row)-1][int(column)-1] = token
    print(f"Computer placed {token} at {row}, {column}")
    return board


def bot_turn(board, tokens):
    """bot placement"""
    while True:
        index_choice = get_easy_bot_choice(board)
        try:
            return try_place(board, index_choice, tokens.bot_token)
        except ValueError as e:
            show_error_message(f"Bot triggered Error: '{e}'")


def get_easy_bot_choice(board):
    """generate random board location choice
    
    get the min and max size of the board
    and generate a random row and column
    """
    min_max = board.min_max()
    min_range = int(min_max["min"])
    max_range = int(min_max["max"])

    row = str(randint(min_range, max_range))
    column = str(randint(min_range, max_range))
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
    """Check for winner
    
    return winner or None
    """
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

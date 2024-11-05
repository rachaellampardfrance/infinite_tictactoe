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
    while created == False:
        try:
            game_board = GameBoard()
            return game_board
        except ValueError as e:
            show_error_message(e)


def set_tokens():
    """Create token object with associated player tokens"""
    created = False
    while created == False:
        try:
            player_token = input("Choose X or O: ").strip().upper()
            player_tokens = Tokens(player_token)
            return player_tokens
        except ValueError as e:
            show_error_message(e)


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
    min = board_range["min"]
    max = board_range["max"]

    row = input(f"select row location {min}-{max}: ")
    column = input(f"select column location {min}-{max}: ")
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
    min = int(min_max["min"])
    max = int(min_max["max"])

    row = str(randint(min, max))
    column = str(randint(min, max))
    return {"row": row, "column": column}



def turn(board, tokens):
    """player turn"""
    print_game(board, tokens)
    winner = check_for_winner(board)
    if winner:
        raise ValueError(winner)
    elif is_stalemate(board):
        raise ValueError("Stalemate!")


def check_for_winner(board):
    """Check for winner
    
    return winner or None
    """
    list = board.list
    winner = ''

    # check any row is all the same token
    for i in range(3):
        if (list[i][0] == list[i][1] == list[i][2] 
            and not list[i][0] == ' '):
            winner = list[i][0]

    #  check any column is all the same token
    for i in range(3):
        if (list[0][i] == list[1][i] == list[2][i] 
            and not list[0][i] == ' '):
            winner = list[0][i]
    
    #  check any diagonal is all the same token
    if (list[0][0] == list[1][1] == list[2][2] 
        and not list[0][0] == ' '):
        winner = list[0][0]
    elif (list[0][2] == list[1][1] == list[2][0] 
          and not list[1][1] == ' '):
        winner = list[1][1]

    if winner:
        return winner
    return None


def is_stalemate(board):
    """check if stalemate"""
    list = board.list

    for i in range(3):
        for j in range(3):
            if list[i][0] == ' ' or list[i][1] == ' ' or list[i][2] == ' ':
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
        elif choice == "N":
            return False


def show_error_message(e):
    """format + show error message"""
    print(f"ERROR: {e}")


def show_win_message(win):
    """format + show winner message"""
    print(f"WINNER! : {win}")


if __name__ == '__main__':
    main()

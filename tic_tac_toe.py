"""This program runs a game of tic tac toe"""
from game_board import GameBoard
from tokens import Tokens
from random import randint


def main():
    # create GameBoard class instance
    # player_tokens = set_tokens()
    # game_board = create_game_board()
    game_board, player_tokens = init_game()
    print_game(game_board, player_tokens)
    
    # game loop
    game_loop(game_board, player_tokens)
        













def init_game():
    board = create_game_board()
    tokens = set_tokens()
    return board, tokens


def create_game_board():
    """create game board class and set player marker"""
    created = False
    while created == False:
        try:
            game_board = GameBoard()
            return game_board
        except ValueError as e:
            show_error_message(e)


def set_tokens():
    """Create tokens to be associated with each player"""
    created = False
    while created == False:
        try:
            player_token = input("Choose X or O: ").strip().upper()
            player_tokens = Tokens(player_token)
            return player_tokens
        except ValueError as e:
            show_error_message(e)


def print_game(board, tokens):
    print(tokens)
    print(board)


def game_loop(board, player_tokens):
    game_on = True
    try:
        while game_on:
                board = user_placement(board, player_tokens)
                turn(board, player_tokens)
                board = easy_bot_turn(board, player_tokens)
                turn(board, player_tokens)
                game_on = game_on_choice()
    except ValueError as win:
        show_win_message(win)


def user_placement(board, player_tokens):
    while True:
        placement_choice = get_user_row_column(board)
        try:
            return try_place(board, placement_choice, player_tokens.user_token)
        except ValueError as e:
            show_error_message(e)


def get_user_row_column(board): 
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
    """board: is the game board object
    location: is a dict containing "min" and "max" keys
    token: is the current players token"""
    row = location["row"]
    column = location["column"]
    board.validate_placement(row, column)
    board.list[int(row)-1][int(column)-1] = token
    return board


def easy_bot_turn(board, player_tokens):
    """basic random placement bot"""

    # get GameBoard index for min, max
    # board placements incase board size changes
    min_max = board.min_max()
    min = int(min_max["min"])
    max = int(min_max["max"])

    while True:
        row = str(randint(min, max))
        column = str(randint(min, max))
        index_choice = {"row": row, "column": column}
        try:
            return try_place(board, index_choice, player_tokens.bot_token)
            # print(f"Computer placed {tokens.bot_token} at {row}, {column}")
        except ValueError as e:
            show_error_message(f"Bot triggered Error: '{e}'")


def turn(board, player_tokens):
    print_game(board, player_tokens)
    winner = check_for_winner(board)
    if winner:
        raise ValueError(winner)


def check_for_winner(board):
    """Check for winner, return winner or None"""
    list = board.list
    winner = ''

    # check if any row is all the same token
    for i in range(3):
        if list[i][0] == list[i][1] == list[i][2] and not list[i][0] == ' ':
            winner = list[i][0]

    #  check if any column is all the same token
    for i in range(3):
        if list[0][i] == list[1][i] == list[2][i] and not list[0][i] == ' ':
            winner = list[0][i]
    
    #  check is any diagonal is all the same token
    if list[0][0] == list[1][1] == list[2][2] and not list[0][0] == ' ':
        winner = list[0][0]
    elif list[0][2] == list[1][1] == list[2][0] and not list[1][1] == ' ':
        winner = list[1][1]

    if winner:
        return format_winner_message(winner)
    return None


def format_winner_message(winner):
    return f"WINNER! : {winner}"


def game_on_choice():
    """Gets user input at the end of each game loop
    for if the user wants to continue playing"""
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
    print(e)


def show_win_message(win):
    print(win)


if __name__ == '__main__':
    main()

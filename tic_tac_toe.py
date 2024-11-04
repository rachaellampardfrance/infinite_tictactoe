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
            print(e)


def set_tokens():
    """Create tokens to be associated with each player"""
    created = False
    while created == False:
        try:
            player_token = input("Choose X or O: ").strip().upper()
            player_tokens = Tokens(player_token)
            return player_tokens
        except ValueError as e:
            print(e)


def print_game(board, tokens):
    print(tokens)
    print(board)


def game_loop(board, player_tokens):
    game_on = True
    while game_on:
        board = user_place(board, player_tokens)
        print_game(board, player_tokens)
        winner = check_for_winner(board.list)
        if winner:
            print(winner)
            game_on = False
            return
        board = easy_bot_turn(board, player_tokens)
        print_game(board, player_tokens)
        winner = check_for_winner(board.list)
        if winner:
            print(winner)
            game_on = False
            return
        game_on = game_on_choice()


def user_place(game_board, player_tokens):
    """Loop until valid user placement is input"""
    
    # get first and last list items of board index for placement range
    board_indexes = '-'.join(str(game_board.index[0]) + str(game_board.index[-1])) 
    while True:
        row = input(f"select row location {board_indexes}: ")
        column = input(f"select column location {board_indexes}: ")
        try:
            # use class function to check placement exists and is free
            if game_board.is_valid_placement(row, column):
                game_board.list[int(row)-1][int(column)-1] = player_tokens.user_token
                return game_board
            else:
                print("placement is already taken, try again")
        except ValueError as e:
            print(e)
    

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


def check_for_winner(game_list):
    """Check for winner, return winner or None"""
    win_text = "WINNER! : "

    # check if any row is all the same token
    for i in range(3):
        if game_list[i][0] == game_list[i][1] == game_list[i][2] and not game_list[i][0] == ' ':
            winner = game_list[i][0]
            return win_text + winner
    #  check if any column is all the same token
    for i in range(3):
        if game_list[0][i] == game_list[1][i] == game_list[2][i] and not game_list[0][i] == ' ':
            winner = game_list[0][i]
            return win_text + winner
    #  check is any diagonal is all the same token
    if game_list[0][0] == game_list[1][1] == game_list[2][2] and not game_list[0][0] == ' ':
        winner = game_list[0][0]
        return win_text + winner
    if game_list[0][2] == game_list[1][1] == game_list[2][0] and not game_list[1][1] == ' ':
        winner = game_list[1][1]
        return win_text + winner
    # if no winner
    return None


def easy_bot_turn(board, tokens):
    """basic random placement bot"""

    # get GameBoard index for min, max
    # board placements incase board size changes
    min = int(board.index[0])
    max = int(board.index[-1])

    while True:
        row = randint(min, max)
        column = randint(min, max)
        try:
            # use class function to check placement exists and is free
            if board.is_valid_placement(str(row), str(column)):
                print(f"Computer placed {tokens.bot_token} at {row}, {column}")
                board.list[row -1][column -1] = tokens.bot_token
                return board
            else:
                print("is not valid bot placement")
                pass
        except ValueError as e:
            print(f"Bot triggered Error: '{e}'")
            pass


if __name__ == '__main__':
    main()

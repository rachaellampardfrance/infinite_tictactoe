"""This program runs a game of tic tac toe"""
from game_board import GameBoard
from random import randint


def main():
    game_board = create_game_board()
    print(game_board)
    # basic moves and board printing
    # create game loop
    # create win condition
    game_on = True
    while game_on:
        game_board = place(game_board)
        print(game_board)
        game_board = easy_bot_turn(game_board)
        print(game_board)
        game_on = game_on_choice()










def create_game_board():
    """create game board class and set player marker"""
    created = False
    while created == False:
        try:
            player = input("Choose X or O: ").strip().upper()
            game_board = GameBoard(player)
            return game_board
        except ValueError as e:
            print(e)


def place(game_board):
    # get first and last list items of board index for range
    board_indexes = '-'.join(str(GameBoard.board_index[0]) + str(GameBoard.board_index[-1])) 
    while True:
        row = input(f"select row location {board_indexes}: ")
        column = input(f"select column location {board_indexes}: ")
        try:
            # use class function to check placement exists and is free
            if game_board.is_valid_placement(row, column):
                game_board.list[int(row)-1][int(column)-1] = game_board.player_token
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







def easy_bot_turn(game_board):
    # create the logic for bot taking turn
    # reading edges to make choices
    min = int(GameBoard.board_index[0])
    max = int(GameBoard.board_index[-1])

    while True:
        row = randint(min, max)
        column = randint(min, max)
        try:
            # use class function to check placement exists and is free
            if game_board.is_valid_placement(str(row), str(column)):
                print(f"Computer placed {game_board.bot_token} at {row}, {column}")
                game_board.list[row -1][column -1] = game_board.bot_token
                return game_board
            else:
                print("is not valid bot placement")
                pass
        except ValueError as e:
            print(f"Bot triggered Error: '{e}'")
            pass

# add in medium and hard bots using
# edge checking logic



if __name__ == '__main__':
    main()

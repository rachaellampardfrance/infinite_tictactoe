from game_board import GameBoard


def main():
    game_board = create_game_board()
    print(game_board)
    game_board = place(game_board)
    print(game_board)
    # game_board.list[1][2] = 'X'
    # print(game_board)

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
    board_indexes = '-'.join(GameBoard.board_index[:1] + GameBoard.board_index[-1:]) 
    while True:
        row = input(f"select row location {board_indexes}: ")
        colum = input(f"select column location {board_indexes}: ")
        try:
            # use class function to check placement exists and is free
            if game_board.is_valid_placement(row, colum):
                game_board.list[int(row)-1][int(colum)-1] = game_board.player
                return game_board
            else:
                print("placement is already taken, try again")
        except ValueError as e:
            print(e)
    
if __name__ == '__main__':
    main()

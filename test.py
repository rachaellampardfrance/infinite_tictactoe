from game_board import GameBoard


def main():
    game_board = create_game_board()
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
    
if __name__ == '__main__':
    main()

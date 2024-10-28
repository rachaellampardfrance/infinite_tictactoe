"""This program is a tic tac toe game"""

# Imports

def main():
    """main program"""
    # main
    game_list = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    # choose player marker
    player = player_mark()
    # place player marker
    game_list[user_place('row')][user_place('column')] = player
    # print current game board
    game_board(game_list)


def player_mark():
    """Player can choose bettween
    defined X or O marker"""
    mark = ' '
    while not mark in ['X', 'O']:
        mark = input("Choose X or O").strip().upper()
        if not mark in ['X', 'O']:
            print(f"{mark} is not a vaild input") 
    return mark


def user_place(location):
    """Player can choose placement location
    by row and column"""

    # Initial
    place = 'False'
    acceptable_range = range(1,4)
    within_range = False

    # Two conditions
    # Digit and within range
    while place.isdigit() == False or within_range == False:
        #  input
        place = input(f"select {location} location 1-3: ")
        # Digit check
        if place.isdigit() == False:
            print(f"{place} is not a digit")
            place = 'False'
        # Range check
        elif int(place) in acceptable_range:
            return int(place) - 1
        print(f"{place} is not a valid placement location")
        within_range = False
        # print(f" user_place {location}: {place}")


def game_board(game_log):
    """Print game board with current placements"""
    div_top = " ___________ "
    div_mid = "|---|---|---|"
    div_bottom = f" {chr(8254)*11} "

    table = f"""
    {div_top}
    | {game_log[0][0]} | {game_log[0][1]} | {game_log[0][2]} |
    {div_mid}
    | {game_log[1][0]} | {game_log[1][1]} | {game_log[1][2]} |
    {div_mid}
    | {game_log[2][0]} | {game_log[2][1]} | {game_log[2][2]} |
    {div_bottom}
    """

    print(table)

if __name__ == '__main__':
    main()
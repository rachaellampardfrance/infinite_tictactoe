from random import randint


class TicTacToeComputer():

    def get_easy_choice(self) -> dict:
        row = randint(0, self.size - 1)
        column = randint(0, self.size - 1)

        print(f"Random placement tried: [{row}][{column}]")
        return {"row": row, "column": column}


    def get_hard_choice(self, tokens):

        checks = [
            (self._try_win, (tokens.player2_token, tokens, 2)),
            (self._try_challenge_player, (tokens.player1_token, tokens, 2)),
            (self._try_best_progress, (tokens.player2_token, tokens, 1))
        ]

        for func, args in checks:
            choice = func(*args)
            if choice:
                print(f"func: {func} args: {args}")
                return choice
        
        return self.get_easy_choice()


    def _try_win(self, token, tokens, count):
        print(f"try win")
        args = (token, tokens, count)
        checks = [
            (self._check_rows)
        ]

        for func in checks:
            choice = func(*args)
            if choice:
                return choice
        

    def _try_challenge_player(self, token, tokens, count):
        print(f"try challenge player")
        args = (token, tokens, count)
        checks = [
            (self._check_rows)
        ]

        for func in checks:
            choice = func(*args)
            if choice:
                return choice


    def _try_best_progress(self, token, tokens, count):
        print("try best progress")
        args = (token, tokens, count)
        checks = [
            (self._check_rows)
        ]

        for func in checks:
            choice = func(*args)
            if choice:
                return choice

    def _check_rows(self, token: str, tokens: object, count: int):
        for i in range(self.size):
            choice = self._check_row(i, token, tokens, count)
            if choice:
                return choice


    def _check_row(self, itr: int, token: str, tokens: object, count: int):
        row_icons: list = []
        column_icons: list = []

        for i in range(self.size):
            row_icons.append(self.list[itr][i])
            column_icons.append(self.list[i][itr])

        if count == 1:
            #  try to make best placement for win where player1 is not in row
            if row_icons.count(token) == count and not tokens.player1_token in row_icons:
                choice = self._consider_row(itr)
                if choice:
                    return choice 
            
            if column_icons.count(token) == count and not tokens.player1_token in column_icons:
                choice = self._consider_column(itr)
                if choice:
                    return choice
            #     # try:
            #         choice["row"], choice["column"] = self._consider_row(itr)
            #         return choice
                # except ValueError:
                #     return
        else:
            if row_icons.count(token) == count and self.default_item in row_icons:
                choice = self._consider_row(itr)
                if choice:
                    return choice
            elif column_icons.count(token) == count and self.default_item in column_icons:
                choice = self._consider_column(itr)
                if choice:
                    return choice

# def _check_row_prevent_win(board: object, itr: int, tokens: object):
#     row_icons: list = []
#     choice = {"row": None, "column": None}

#     for i in range(board.size):
#         row_icons.append(board.list[itr][i])

#     print(row_icons)

#     if row_icons.count(tokens.player1_token) == 2:
#         choice["row"], choice["column"] = _consider_row(board, itr)
#         print("row, hard choice: challenge player")
#         return choice

#     elif row_icons.count(tokens.player2_token) == 2:
#         choice["row"], choice["column"] = _consider_row(board, itr)
#         print("row, hard choice: try win")
#         return choice
    
#     elif row_icons.count(tokens.player2_token) == 1:
#         choice["row"], choice["column"] = _consider_row(board, itr)
#         print("row, hard choice: best progress choice")
#         return choice

#     else:
#         choice["row"], choice["column"] = _random_placement(board)
#         print("row, hard choice: random choice")
#         return choice


    def _consider_row(self, j: int) -> tuple:
        """cycle over row to find free space"""
        print(f"considering row {j}")
        for i in range(self.size):
            row_icon = self.list[j][i]
            print(f"row icon[{j}][{i}]: '{row_icon}'")
            if row_icon == self.default_item:
                print(f"success")
                return {"row": j, "column": i}
            print(f"failed consideration")


    def _consider_column(self, j: int) -> tuple:
        """cycle over row to find free space"""
        print(f"considering column {j}")
        for i in range(self.size):
            row_icon = self.list[i][j]
            print(f"row icon[{i}][{j}]: '{row_icon}'")
            if row_icon == self.default_item:
                print(f"success")
                return {"row": i, "column": j}
            print(f"failed consideration")

    # def _find_free_space(self, j: int) -> tuple:
    #     """cycle over row to find free space"""
    #     for i in range(self.size):
    #         row_icon = self.list[j][i]
    #         if row_icon == self.default_item:
    #             return j, i
    #     raise ValueError()

# def _random_placement(board: object) -> tuple:
#     choice = {"row": None, "column": None}

#     choice["row"], choice["column"] = _get_random_placement(board)

#     return choice


# def _get_random_placement(board: object):
#     row = randint(0, board.size)
#     column = randint(0, board.size)
#     print(f"row: {row} column: {column}")
#     return row, column



def _check_for_winner(self) -> None:
    """bubble GameEndError if winner found"""
    self._check_rows_columns()
    self._check_top_right_diagonal()
    self._check_bottom_right_diagonal()

def _check_rows_columns(self) -> None:
    """bubble GameEndError if winner found"""
    for i in range(self.size):
        self._check_row_column( i)
        
def _check_row_column(self, itr: int) -> None:
    """raises GameEndError if any row or column is all the same token
    
    :param board: A GameBoard object
    :param itr: 'int' for iteration
    """
    row_icons: set = set()
    column__icons: set = set()

    for i in range(self.size):
        row_icons.add(self.list[itr][i])
        column__icons.add(self.list[i][itr])
    if len(row_icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in row_icons:
        raise GameEndError(user_error_message("4", row_icons.pop()))
    if len(column__icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in column__icons:
        raise GameEndError(user_error_message("4", column__icons.pop()))

def _check_top_right_diagonal(self) -> None:
    """raises GameEndError if top right down diagonal is all the same token"""
    icons: set = set()
    for i in range(self.size):
        icons.add(self.list[i][i])
    if len(icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in icons:
        raise GameEndError(user_error_message("4", icons.pop()))

def _check_bottom_right_diagonal(self) -> None:
    """raises GameEndError if bottom right up diagonal is all the same token"""
    icons: set = set()
    size: int = self.size - 1
    for i in range(self.size):
        icons.add(self.list[i][size - i])
    if len(icons) == 1 and not GameBoard.DEFAULT_LIST_ITEM in icons:
        raise GameEndError(user_error_message("4", icons.pop()))


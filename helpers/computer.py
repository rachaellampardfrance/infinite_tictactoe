from random import randint


class TicTacToeComputer():
    """holds parent functions for the TicTacToeBoard
    class"""

    def get_easy_choice(self) -> dict:
        """generate a random choice by board size"""
        row = randint(0, self.size - 1)
        column = randint(0, self.size - 1)

        return {"row": row, "column": column}


    def get_hard_choice(self, tokens: object) -> dict:
        """return a choice by order of priority"""

        # functions for each positional check
        func = [
            (self._consider_straights),
            (self._consider_top_diagonal),
            (self._consider_bottom_diagonal)
        ]
        # argument order, try win, try prevent player from...
        # ...winning, try best progress
        args = [
            (tokens.player2_token, tokens, 2, 'row'),
            (tokens.player2_token, tokens, 2),
            (tokens.player1_token, tokens, 2),
            (tokens.player2_token, tokens, 1)
        ]

        # by argument, run all functions
        for arg in args:
            for fun in func:
                print(fun, arg)
                # do not pass 'row' to diagonals
                if not func == self._consider_straights and arg == (tokens.player2_token, tokens, 2, 'row'):
                    continue
                choice = fun(*arg)
                if choice:
                    return choice
        
        return self.get_easy_choice()


    def _consider_straights(self, token: str, tokens: object, count: int, position: str = 'column') -> dict:
        """loop over each row/column"""
        for i in range(self.size):
            choice: dict | None = self._consider_straight(i, token, tokens, count, position)
            if choice:
                return choice


    def _consider_straight(self, itr: int, token: str, tokens: object, count: int, position: str) -> dict:
        """check row by priority """
        icons: list = self._generate_icons(itr, position)
        matches_priority = (icons.count(token) == count)
        player_present = (tokens.player1_token in icons)
        is_free_space = (self.default_item in icons)

        if count == 1:
            #  try to make best placement to progress, where player is not in row
            if matches_priority and not player_present:
                choice: dict | None = self._try_straight(itr, position)
                if choice:
                    return choice 

        else:
            # by priority try to win or prevent the player from winning
            if matches_priority and is_free_space:
                choice: dict | None = self._try_straight(itr, position)
                if choice:
                    return choice


    def _generate_icons(self, itr: int, position: str) -> list:
        icons: list = []
        for i in range(self.size):
            if position == 'row':
                icons.append(self.list[itr][i])
            else:
                icons.append(self.list[i][itr])
        return icons


    def _try_straight(self, j: int, position: str = "column") -> dict:
        """cycle over row to find free space"""
        for i in range(self.size):
            if position == 'row':
                if self.list[j][i] == self.default_item:
                    return {"row": j, "column": i}
            else:
                if self.list[i][j] == self.default_item:
                    return {"row": i, "column": j}


    def _consider_top_diagonal(self, token: str, tokens: object, count: int) -> dict:
        icons = []

        for i in range(self.size):
            icons.append(self.list[i][i])

        if count == 1:
            if icons.count(token) == count and not tokens.player1_token in icons:
                choice: dict | None = self._try_top_diagonal()
                if choice:
                    return choice
        else:
            if icons.count(token) == count and self.default_item in icons:
                choice: dict | None = self._try_top_diagonal()
                if choice:
                    return choice
                

    def _try_top_diagonal(self) -> dict:
        """for top left diagonal checks for
        free space to drop marker"""
        for i in range(self.size):
            icon: str = self.list[i][i] 
            if icon == self.default_item:
                return {"row": i, "column": i}


    def _consider_bottom_diagonal(self, token: str, tokens: object, count: int) -> dict:
        icons: list = []
        size: int = self.size - 1

        for i in range(self.size):
            icons.append(self.list[i][size - i])
        
        if count == 1:
            if icons.count(token) == count and not tokens.player1_token in icons:
                choice: dict | None = self._try_bottom_diagonal()
                if choice:
                    return choice
        else:
            if icons.count(token) == count and self.default_item in icons:
                choice: dict | None = self._try_bottom_diagonal()
                if choice:
                    return choice
            
    def _try_bottom_diagonal(self) -> dict:
        """for bottom left diagonal checks for
        free space to drop marker"""
        size: int = self.size - 1
        for i in range(self.size):
            j = size - i
            icon: str = self.list[i][j]
            if icon == self.default_item:
                return {"row": i, "column": j}
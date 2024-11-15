"""TicTacToe computer player logic that parents the TicTacToeBoard class"""
from random import randint


class TicTacToeComputer():
    """holds parent logic functions for the computer player 
    for the TicTacToeBoard class"""

    def get_easy_choice(self) -> dict:
        """generate a random choice by board size"""
        row = randint(0, self.size - 1)
        column = randint(0, self.size - 1)

        return {"row": row, "column": column}


    def get_hard_choice(
            self,
            tokens: object) -> dict:
        """:returns: a 'dict' token placement choice by order of priority"""
        args = self._generate_priorities(tokens)
        func = self._consider_lines

        for arg in args:
            choice = func(*arg)
            if choice:
                return choice

        return self.get_easy_choice()


    def _generate_priorities(
            self,
            tokens: object) -> list:
        """generate func arguments in order of priority

        :returns: type 'list' of tuples containing arguments"""
        priorities: list = []
        positions: list = ['row', 'column', 'top diagonal', 'bottom diagonal']

        for i in reversed(range(1, self.size)):
            for position in positions:
                # make the winning or best progress move
                priorities.append((tokens.player2_token, tokens, i, position))
            for position in positions:
                # make the best prevent player win or challenge move
                priorities.append((tokens.player1_token, tokens, i, position))

        return priorities


    def _consider_lines(
            self,
            token: str,
            tokens: object,
            priority: int,
            position: str) -> dict:
        """:returns: placement location"""
        args = (token, tokens, priority, position)
        if position in ['row', 'column']:
            for i in range(self.size):
                choice = self._consider_line(*args, itr=i)
                if choice:
                    return choice
            return None
        # used for diagonal checks  as doesn't need recursive checking
        return self._consider_line(*args)


    def _consider_line(
            self,
            *args,
            itr: int | None = None) -> dict:
        """:returns: placement location"""
        token, tokens, priority, position = args
        indexed_icons: list = self._generate_indexed_icons(position, itr)
        matches_priority = self._matches_requirements(indexed_icons, token, tokens, priority)

        if matches_priority:
            return self._get_location(indexed_icons)
        return None


    def _generate_indexed_icons(
            self,
            position: str,
            itr: int | None = None) -> list:
        """generate a list of icons and their index locations
        
        :param position: type 'str'. valid arguments; 'row', 
        'column', 'top diagonal', 'bottom diagonal'.
        :param itr: type 'int' that can be assigned to check a
        specific row or column at the int index.
        """
        if position == 'row':
            return self._generate_row_index_items(itr)
        if position == 'column':
            return self._generate_column_index_items(itr)
        if position == 'top diagonal':
            return self._generate_top_diagonal_index_items()
        if position == 'bottom diagonal':
            return self._generate_bottom_diagonal_index_items()

        raise ValueError


    def _generate_row_index_items(self, itr: int) -> list:
        indexed_icons:list = []

        for i in range(self.size):
            indexed_icons.append((self.list[itr][i], (itr, i)))
        return indexed_icons

    def _generate_column_index_items(self, itr: int) -> list:
        indexed_icons:list = []

        for i in range(self.size):
            indexed_icons.append((self.list[i][itr], (i, itr)))
        return indexed_icons

    def _generate_top_diagonal_index_items(self) -> list:
        indexed_icons:list = []

        for i in range(self.size):
            indexed_icons.append((self.list[i][i], (i, i)))
        return indexed_icons

    def _generate_bottom_diagonal_index_items(self) -> list:
        indexed_icons:list = []
        size: int = self.size - 1

        for i in range(self.size):
            indexed_icons.append((self.list[i][size - i], (i, size - i)))
        return indexed_icons


    def _matches_requirements(
            self,
            indexed_icons: list,
            token: str,
            tokens: list,
            priority: int) -> bool:
        """:param indexed_icons: 'list' of tuples containing an icon
        'str' and a tuple (i, j) of index location
        :param priority: the count of tokens needed to match the priority
        """
        icons: list = self._unpack_icons(indexed_icons)

        if not self._is_priority_match(icons, token, priority):
            return False
        if not self._is_free_space(icons):
            return False
        if self._is_opposite_token_present(icons, token, tokens):
            return False

        return True

    def _unpack_icons(self, indexed_icons: list) -> list:
        """unpack icons from list of tuples with icons and index's

        :param icons: 'list' of tuples with icon 'str'
        and tuple (i, j) of icons index location"""
        return [icon for icon, _ in indexed_icons]

    def _is_free_space(self, icons: list) -> bool:
        return self.default_item in icons

    def _is_opposite_token_present(
            self,
            icons: list,
            token: str,
            tokens: object) -> bool:
        opposite_token = [tokens.player1_token, tokens.player2_token]
        opposite_token.remove(token)
        return opposite_token[0] in icons

    def _is_priority_match(
            self,
            icons: list,
            token: str,
            priority: int) -> bool:
        return icons.count(token) == priority


    def _get_location(self, indexed_icons: list) -> dict:
        """get placement location from free space icon

        :param icons: 'list' of tuples with icon 'str'
        and tuple (i, j) of icons index location
        
        :returns: dict of keys 'row' and 'column' with
        corresponding index values"""
        for icon, index in indexed_icons:
            if icon == self.default_item:
                return {"row": index[0], "column": index[1]}
        return None

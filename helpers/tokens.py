"""create token class and logic"""
from helpers.messages.messages import user_error_message
from helpers.validation import validate_str

class Tokens:

    PLAYER_TOKENS: list = ['X', 'O']

    def __init__(self, player1_token: str ='X') -> object:
        self.player1_token: str = player1_token
        self.player2_token: str = self.get_player2_token()

    def __str__(self) -> str:
        tokens = (f"Player: {self.player1_token}\n"
        f"Computer: {self.player2_token}")
        return tokens
    

    def get_player2_token(self) -> str:
        """set player2 token dependant on player1 token
        
        :returns: 'str' of player2 token"""
        self.valid_token(self.player1_token)

        if self.player1_token == Tokens.PLAYER_TOKENS[0]:
            return Tokens.PLAYER_TOKENS[1]
        return Tokens.PLAYER_TOKENS[0]
        

    @classmethod
    def valid_token(cls, token: str) -> None:
        if not token in cls.PLAYER_TOKENS:
            raise ValueError(user_error_message(
                "7",
                token,
                cls.PLAYER_TOKENS[0],
                cls.PLAYER_TOKENS[1])
                )


    @property
    def player1_token(self) -> str:
        return self._player1_token
    @player1_token.setter
    def player1_token(self, player1_token: str) -> None:
        validate_str(player1_token)
        Tokens.valid_token(player1_token)
         
        self._player1_token = player1_token
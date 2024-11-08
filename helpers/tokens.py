"""create token class and logic"""
from helpers.messages.messages import user_error_message
from helpers.validation import validate_str

class Tokens:

    PLAYER_TOKENS: list = ['X', 'O']

    def __init__(self, user_token: str ='X') -> object:
        self.user_token: str = user_token
        self.bot_token: str = self.get_bot_token()

    def __str__(self) -> str:
        tokens = (f"Player: {self.user_token}\n"
        f"Computer: {self.bot_token}")
        return tokens
    

    def get_bot_token(self) -> str:
        """set player2 token dependant on player1 token
        
        :returns: 'str' of player2 token"""
        self.valid_token(self.user_token)

        if self.user_token == Tokens.PLAYER_TOKENS[0]:
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
    def user_token(self) -> str:
        return self._user_token
    @user_token.setter
    def user_token(self, user_token: str) -> None:
        validate_str(user_token)
        Tokens.valid_token(user_token)
         
        self._user_token = user_token
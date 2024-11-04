"""create token class and logic"""
from validation import validate_str, validate_digit, validate_int

class Tokens:

    PLAYER_TOKENS = ['X', 'O']

    def __init__(self, user_token='X'):
        self.user_token = user_token
        self.bot_token = self.get_bot_token()

    def __str__(self):
        tokens = (f"Player: {self.user_token}\n"
        f"Computer: {self.bot_token}")
        return tokens
    

    def get_bot_token(self):
        self.validate_user_token()

        if self.user_token == 'X':
            return 'O'
        return 'X'
    

    def validate_user_token(self):
        if self.user_token not in Tokens.PLAYER_TOKENS:
            raise ValueError("Player token is not set to 'X' or 'O'")
        

    @classmethod
    def valid_token(cls, token):
        if not token in cls.PLAYER_TOKENS:
            raise ValueError(f"'{token}' is not a valid player token. Valid tokens 'X', 'O'")


    @property
    def user_token(self):
        return self._user_token
    @user_token.setter
    def user_token(self, user_token):
        Tokens.valid_token(user_token)
         
        self._user_token = user_token
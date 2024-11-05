"""create token class and logic"""
from messages import error_message
from validation import validate_str

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
        # self.validate_user_token()
        self.valid_token(self.user_token)

        available_tokens = Tokens.PLAYER_TOKENS
        available_tokens.remove(self.user_token)
        return available_tokens[0]
        

    @classmethod
    def valid_token(cls, token):
        if not token in cls.PLAYER_TOKENS:
            raise ValueError(error_message(
                "17",
                token,
                Tokens.PLAYER_TOKENS[0],
                Tokens.PLAYER_TOKENS[1])
                )


    @property
    def user_token(self):
        return self._user_token
    @user_token.setter
    def user_token(self, user_token):
        validate_str(user_token)
        Tokens.valid_token(user_token)
         
        self._user_token = user_token
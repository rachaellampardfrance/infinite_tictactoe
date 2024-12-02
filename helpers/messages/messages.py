"""Messages for tic tac toe program"""

ERROR_MESSAGES = {
    "1": "'size' must be between {} - {} inclusive",
    "6": "error_message() was given {} Error Arguments but was expecting {}.",
    "3": "{} must be a positive integer",
}

def error_message(message_code: str, *details: any) -> str:
    """:returns: Formatted Error message from code"""
    message: str = ERROR_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        raise ValueError(ERROR_MESSAGES["2", message.count("{}"), len(details)])
    return message


USER_MESSAGES = {
    "1": "Choose {} or {}: ",
    "2": "{} select y location {}-{}: ",
    "3": "{} select x location {}-{}: ",
    "4": "'ctrl + C' to exit game at any time...\n\
Input column and row like you would \
x, y coordinates for a graph.\n",
    "5": "Infinite Tic Tac Toe",
    "6": "Closing...",
    "7": "2 player or play against the computer? 2P / C : ",
    "8": "Choose board size {}-{}: ",
    "9": "Choose difficulty easy/hard: ",
}

def user_message(message_code: str, *details: any) -> str:
    """:returns: Formatted user message from code"""
    message: str = USER_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        raise ValueError(ERROR_MESSAGES["6", message.count("{}"), len(details)])
    return message


USER_ERROR_MESSAGES = {
    "1": "Input must be a digit",
    "2": "placement is already taken, try again",
    "3": "Not a board location",
    "4": "WINNER! {}",
    "5": "Stalemate!",
    "6": "Game End: {}",
    "7": "'{}' is not a valid player token. Valid tokens {}, {}",
    "8": "Input cannot be empty",
}

def user_error_message(message_code: str, *details: any) -> str:
    """:returns: Formatted user error message from code"""
    message: str = USER_ERROR_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        raise ValueError(ERROR_MESSAGES["6", message.count("{}"), len(details)])
    return message


def show_message(e: str) -> None:
    """prints message to user"""
    print(e)

def game_end_error_message(e: str) -> None:
    """prints game end message with causation"""
    print(user_error_message("6", e))

def exit_message() -> None:
    """prints exit program message"""
    print(user_message("6"))

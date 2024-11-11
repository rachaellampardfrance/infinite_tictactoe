"""Messages for tic tac toe program"""

ERROR_MESSAGES = {
    "1": "'size' must be between {} - {} inclusive",
    "6": "ERROR: error_message() was given {} Error Arguments but was expecting {}.",
    "3": "{} must be a positive integer",
}

def error_message(message_code: str, *details: any) -> str:
    """:returns: Formatted Error message from code"""
    message: str = ERROR_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        else:
            raise ValueError(ERROR_MESSAGES["2", message.count("{}"), len(details)])
    return message


USER_MESSAGES = {
    "1": "Choose {} or {}: ",
    "2": "select row location {}-{}: ",
    "3": "select column location {}-{}: ",
    "4": "Continue playing Y/N? ",
    "5": "{} is not a valid option",
    "6": "Closing...",
}

def user_message(message_code: str, *details: any) -> str:
    """:returns: Formatted user message from code"""
    message: str = USER_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        else:
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
    "8": "Input cannot be empty"
}

def user_error_message(message_code: str, *details: any) -> str:
    """:returns: Formatted user error message from code"""
    message: str = USER_ERROR_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        else:
            raise ValueError(ERROR_MESSAGES["6", message.count("{}"), len(details)])
    return message
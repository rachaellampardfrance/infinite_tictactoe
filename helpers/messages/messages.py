"""Messages for tic tac toe program"""

ERROR_MESSAGES = {
    "1": "validate_str() takes at least 1 argument but got 0",
    "2": "'{}' is not of type 'str'",
    "3": "validate_int() takes at least 1 argument but got 0",
    "4": "'{}' is not of type 'int'",
    "5": "'size' must be between {} - {} inclusive",
    "6": "ERROR: error_message() was given {} Error Arguments but was expecting {}.",
    "7": "Bot triggered Error: '{}'",
    "8": "ERROR: {}",
    "9": "ValueError: {}",
    "10": "TypeError: {}",
    "11": "validate_positive_int() takes at least 1 argument but got 0",
    "12": "{} is not a positive integer",
}

def error_message(message_code: str, *details: any) -> str:
    """:returns: Formatted Error message from code"""
    message: str = ERROR_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        else:
            raise ValueError(ERROR_MESSAGES["6", message.count("{}"), len(details)])
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
    "1": "'{}' is not a digit",
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
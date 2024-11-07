"""Messages for tic tac toe program"""

ERROR_MESSAGES = {
    "1": "validate_str() takes at least 1 argument but got 0",
    "2": "'{}' is not of type 'str'",
    "3": "'{}' is not a digit",
    "4": "validate_int() takes at least 1 argument but got 0",
    "5": "'{}' is not of type 'int'",

    "6": "placement is already taken, try again",
    "7": "Not a board location",
    "8": "'size' must be between {} - {} inclusive",
    "9": "ERROR: error_message() was given {} Error Arguments but was expecting {}.",

    "10": "Bot triggered Error: '{}'",

    "11": "WINNER! {}",
    "12": "Stalemate!",

    "13": "ERROR: {}",
    "14": "ValueError: {}",
    "15": "TypeError: {}",
    "16": "Game End: {}",

    "17": "'{}' is not a valid player token. Valid tokens {}, {}",
    "18": "validate_positive_int() takes at least 1 argument but got 0",
    "19": "{} is not a positive integer",
}

def error_message(message_code, *details):
    """Formatted Error codes"""
    message = ERROR_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        else:
            raise ValueError(ERROR_MESSAGES["8", message.count("{}"), len(details)])
    return message


USER_MESSAGES = {
    "1": "Choose {} or {}: ",
    "2": "select row location {}-{}: ",
    "3": "select column location {}-{}: ",
    "4": "Continue playing Y/N? ",
    "5": "{} is not a valid option",
    "6": "Closing...",
}

def user_message(message_code, *details):
    """Formatted Error codes"""
    message = USER_MESSAGES.get(message_code, "Unknown Message")
    if "{}" in message:
        if message.count("{}") == len(details):
            return message.format(*details)
        else:
            raise ValueError(USER_MESSAGES["8", message.count("{}"), len(details)])
    return message
"""Messages for tic tac toe program"""

ERROR_MESSAGES = {
    "1": "validate_str function expected at least one argument but got none",
    "2": "'{}' is not of type 'str'",
    "3": "'{}' is not a digit",
    "4": "validate_int expected at least one argument but got none",
    "5": "'{}' is not of type 'int'",
}

def error_message(error_code, details=""):
    """Formatted Error codes"""
    message = ERROR_MESSAGES.get(error_code, "Unknown Error")
    if "{}" in message:
        return message.format(details)
    return message
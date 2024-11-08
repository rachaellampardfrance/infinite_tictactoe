from helpers.messages.messages import error_message, user_error_message


def validate_str(*items: any):
    """validates all items are strings"""
    if not is_items(*items):
        raise TypeError(error_message("1"))
    
    for item in items:
        if not type(item) is str:
            raise TypeError(error_message("2", type(item).__name__))
        elif not item:
            raise TypeError(user_error_message("8"))


def validate_digit(*items: any):
    """validates all items are strings and digits"""
    validate_str(*items)

    for item in items:
        if not item.isdigit():
            raise ValueError(user_error_message("1", item))


def validate_int(*items: any):
    """validates all items are ints"""
    if not is_items(*items):
        raise TypeError(error_message("3"))
    
    for item in items:
        if not type(item) is int:
            raise TypeError(error_message("4", type(item).__name__))


def validate_positive_int(*items: any):
    """validates all items are ints and positive"""
    if not is_items(*items):
        raise TypeError(error_message("11"))
    
    validate_int(*items)
    
    for item in items:
        if item < 1:
            raise ValueError(error_message("12", item))


def is_items(*items: any) -> bool:
    if not items:
        return False
    return True
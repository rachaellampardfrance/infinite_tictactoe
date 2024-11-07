from helpers.messages.messages import error_message


def validate_str(*items):
    """validates all items are strings"""
    if not items:
        raise TypeError(error_message("1"))
    
    for item in items:
        if not type(item) is str:
            raise TypeError(error_message("2", type(item).__name__))


def validate_digit(*items):
    """validates all items are strings and digits"""
    validate_str(*items)
    for item in items:
        if not item.isdigit():
            raise ValueError(error_message("3", item))


def validate_int(*items):
    """validates all items are ints"""
    if not items:
        raise TypeError(error_message("4"))
    
    for item in items:
        if not type(item) is int:
            raise TypeError(error_message("5", type(item).__name__))


def validate_positive_int(*items):
    """validates all items are ints and positive"""
    if not items:
        raise TypeError(error_message("18"))
    
    validate_int(*items)
    
    for item in items:
        if item < 1:
            raise ValueError(error_message("19", item))
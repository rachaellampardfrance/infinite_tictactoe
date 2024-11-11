from helpers.messages.messages import user_error_message


def validate_digit(item: any):
    """validates all items are strings and digits"""
    if not item.isdigit():
        raise ValueError(user_error_message("1", item))


def item_exists(item: any):
    if not item:
        raise ValueError(user_error_message("8"))
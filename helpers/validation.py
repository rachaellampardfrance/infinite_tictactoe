"""helper functions for main main.py"""
from helpers.messages.messages import user_error_message

def validate_digit(item: any):
    """validate argument is a digit"""
    if not item.isdigit():
        raise ValueError(user_error_message("1"))

def item_exists(item: any):
    """validate argument is not None"""
    if not item:
        raise ValueError(user_error_message("8"))

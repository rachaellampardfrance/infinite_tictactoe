def validate_str(*items):
    if not items:
        raise TypeError(f"validate_ str expected at least one argument but got none")
    
    for item in items:
        if not type(item) is str:
            raise TypeError(f"'{type(item).__name__}' is not of type 'str'")

def validate_digit(*items):
    validate_str(*items)
    for item in items:
        if not item.isdigit():
            raise ValueError(f"'{item}' is not a digit")
        
def validate_int(*items):
    if not items:
        raise TypeError(f"validate_int expected at least one argument but got none")
    
    for item in items:
        if not type(item) is int:
            raise TypeError(f"'{type(item).__name__}' is not of type 'int'")
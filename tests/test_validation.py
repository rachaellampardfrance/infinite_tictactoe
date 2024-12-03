from helpers.validation import validate_digit, item_exists
import pytest

def test_validate_digit():
    with pytest.raises(ValueError, match="Input must be a digit"):
        validate_digit('a')
    with pytest.raises(ValueError, match="Input must be a digit"):
        validate_digit('!')
    with pytest.raises(ValueError, match="Input must be a digit"):
        validate_digit('1as')
    with pytest.raises(ValueError, match="Input must be a digit"):
        validate_digit('')
    
def test_validate_digit_raises_no_exception():
    try:
        validate_digit('1')
    except:
        assert False, "validate_digit('1') raised an exception"

def test_item_exists():
    with pytest.raises(ValueError, match="Input cannot be empty"):
        item_exists('')

def test_item_exists_raises_no_exception():
    try:
        item_exists("1")
    except:
        assert False, "item_exists('1') raised an exception"
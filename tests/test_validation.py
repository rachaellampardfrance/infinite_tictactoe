from validation import validate_digit, validate_str
import pytest

def test_validate_str():
    with pytest.raises(ValueError, match="'int' is not of type 'str'"):
        validate_str(1)
    with pytest.raises(ValueError, match="'int' is not of type 'str'"):
        validate_str('d', 1)
    with pytest.raises(ValueError, match="'list' is not of type 'str'"):
        validate_str([1, 2, 3])
    with pytest.raises(ValueError, match="'list' is not of type 'str'"):
        validate_str('1', [1, 2, 3])
    
def test_validate_str_raises_no_exception():
    try:
        validate_str('a')
    except:
        assert False, "'a' raised an exception"

    try:
        validate_str('a', 'b')
    except:
        assert False, "'a', 'b' raised an exception"

    try:
        validate_str('1')
    except:
        assert False, "'1' raised an exception"


def test_validate_digit():
    with pytest.raises(ValueError, match="'a' is not a digit"):
        validate_digit('a')
    with pytest.raises(ValueError, match="'!' is not a digit"):
        validate_digit('!')
    with pytest.raises(ValueError, match="'1as' is not a digit"):
        validate_digit('1as')
    with pytest.raises(ValueError, match="'' is not a digit"):
        validate_digit('')
    
def test_validate_digit_raises_no_exception():
    try:
        validate_digit('1')
    except:
        assert False, "'1' raised an exception"

    try:
        validate_digit('1', '2')
    except:
        assert False, "'1', '2' raised an exception"

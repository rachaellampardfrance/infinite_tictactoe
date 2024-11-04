"""Tests for setting player game tokens"""
from tokens import Tokens
import pytest


def test_init():
    """correct player and bot tokens set"""
    tokens = Tokens('X') 
    assert tokens.user_token == 'X' and tokens.bot_token == 'O'
    tokens = Tokens('O')
    assert tokens.user_token == 'O' and tokens.bot_token == 'X'
    tokens = Tokens()
    assert tokens.user_token == 'X' and tokens.bot_token == 'O'


def test_player_token():
    """player token sets token == the argument"""
    # correct player token assigned 
    tokens = Tokens('X')
    assert tokens.user_token == 'X'
    tokens = Tokens('O')
    assert tokens.user_token == 'O'

    # raises errors: invalid player token
    with pytest.raises(ValueError, match="'1' is not a valid player token. Valid tokens 'X', 'O'"):
        tokens = Tokens('1')
    with pytest.raises(ValueError, match="'a' is not a valid player token. Valid tokens 'X', 'O'"):
        tokens = Tokens('a')
    with pytest.raises(ValueError, match="'!' is not a valid player token. Valid tokens 'X', 'O'"):
        tokens = Tokens('!')

    # raises errors: invalid data type
    with pytest.raises(ValueError, match="'int' is not of type 'str'"):
        tokens = Tokens(1) 
    with pytest.raises(ValueError, match="'list' is not of type 'str'"):
        tokens = Tokens([]) 
    with pytest.raises(ValueError, match="'dict' is not of type 'str'"):
        tokens = Tokens({}) 
    with pytest.raises(ValueError, match="'tuple' is not of type 'str'"):
        tokens = Tokens(()) 


def test_get_bot_token():
    """should assign opposite token from player"""

    # correct bot token assignment
    tokens = Tokens()
    assert tokens.bot_token == 'O'
    tokens = Tokens('X')
    assert tokens.bot_token == 'O'
    tokens = Tokens('O')
    assert tokens.bot_token == 'X'
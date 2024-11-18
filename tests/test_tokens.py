"""Tests for setting player game tokens"""
from helpers.tokens import Tokens
import pytest


def test_init():
    """correct player and bot tokens set"""
    tokens = Tokens('X') 
    assert tokens.player1_token == 'X' and tokens.player2_token == 'O'
    tokens = Tokens('O')
    assert tokens.player1_token == 'O' and tokens.player2_token == 'X'
    tokens = Tokens()
    assert tokens.player1_token == 'X' and tokens.player2_token == 'O'


def test_player_token():
    """player token sets token == the argument"""
    # correct player token assigned 
    tokens = Tokens('X')
    assert tokens.player1_token == 'X'
    tokens = Tokens('O')
    assert tokens.player1_token == 'O'

    # raises errors: invalid player token
    with pytest.raises(ValueError, match="'1' is not a valid player token. Valid tokens X, O"):
        tokens = Tokens('1')
    with pytest.raises(ValueError, match="'a' is not a valid player token. Valid tokens X, O"):
        tokens = Tokens('a')
    with pytest.raises(ValueError, match="'!' is not a valid player token. Valid tokens X, O"):
        tokens = Tokens('!')


def test_get_bot_token():
    """should assign opposite token from player"""

    # correct bot token assignment
    tokens = Tokens()
    assert tokens.player2_token == 'O'
    tokens = Tokens('X')
    assert tokens.player2_token == 'O'
    tokens = Tokens('O')
    assert tokens.player2_token == 'X'

def test_valid_token():
    
    try:
        Tokens.valid_token('X')
    except:
        assert False, "'X' raised an exception"

    try:
        Tokens.valid_token('O')
    except:
        assert False, "'O' raised an exception"

    with pytest.raises(ValueError, match="'1' is not a valid player token. Valid tokens X, O"):
        Tokens.valid_token('1')


def test_str():

    tokens = Tokens('X')
    assert tokens.__str__() == (
        "Player: X\n"
        "Computer: O")
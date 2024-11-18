"""Tests for setting player game tokens"""
from helpers.tokens import Tokens
from helpers.messages.messages import user_error_message
import pytest


def test_init():
    """correct player and bot tokens set"""
    tokens = Tokens('X') 
    assert (tokens.player1_token == 'X'
            and tokens.player2_token == 'O'
            and tokens.users['1'] == 'Player 1'
            and tokens.users['2'] == 'Player 2'
            )
    tokens = Tokens('O', 'Computer')
    assert (tokens.player1_token == 'O'
            and tokens.player2_token == 'X'
            and tokens.users['1'] == 'Player 1'
            and tokens.users['2'] == 'Computer'
            )
    tokens = Tokens()
    assert (tokens.player1_token == 'X'
            and tokens.player2_token == 'O'
            and tokens.users['1'] == 'Player 1'
            and tokens.users['2'] == 'Player 2'
            )


def test_valid_token_raises_no_exception():
    """valid tokens raise no exceptions"""
    try:
        Tokens.valid_token('X')
    except:
        assert False, "valid_token('X') raised an exception"

    try:
        Tokens.valid_token('O')
    except:
        assert False, "valid_token('O') raised an exception"

def test_valid_token_raises_exception():
    """invalid tokens raises error"""
    with pytest.raises(
        ValueError, 
        match=user_error_message(
            "7",
            '1',
            Tokens.PLAYER_TOKENS[0],
            Tokens.PLAYER_TOKENS[1]
        )):
        Tokens.valid_token('1')


def test_str():

    tokens = Tokens('X')
    assert tokens.__str__() == (
        "Player 1: X\n"
        "Player 2: O")
    
    tokens = Tokens('O')
    assert tokens.__str__() == (
        "Player 1: O\n"
        "Player 2: X")
    
    tokens = Tokens('X', 'Computer')
    assert tokens.__str__() == (
        "Player 1: X\n"
        "Computer: O")
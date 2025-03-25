'''Task: Validate a Username
Only contains letters, numbers, and underscores (_).
Starts with a letter.
Has a length between 4 and 12 characters.
'''

import re

def is_valid_username(name):

    if not isinstance(name, str):
        raise TypeError("Please provide a string as an input")

    if not len(name) > 4 and len(name) < 12:
        return False
    if not re.search(r'[a-zA-Z0-9_]', name):
        return False
    if not re.search(r'[A-Z]', name[0]):
        return False

    return True

def test_is_valid_username_first_sign():
    assert is_valid_username("Aty@@768") == True

def test_is_valid_username_length():
    assert is_valid_username("123") == False
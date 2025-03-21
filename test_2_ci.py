'''Task: Validate a Username
Write a Python function is_valid_username(username: str) -> bool that checks whether a given username meets the following conditions:

Only contains letters, numbers, and underscores (_).
Starts with a letter.
Has a length between 5 and 15 characters.

Write test cases to verify the correctness of the function.'''

import re

def is_valid_username(name):

    if not isinstance(name, str):
        raise TypeError("Please provide a string as an input")

    if not len(name) > 5 and len(name) < 15:
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

from scripts.palindrome import palindrome

def test_palindrome():
    assert palindrome("koala") is False
    assert palindrome("mamam") is True
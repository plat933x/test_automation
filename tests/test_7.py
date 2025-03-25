from scripts.palindrome import palindrome

def test_palindrome():
    assert palindrome("koala") == False
    assert palindrome("mamam") == True
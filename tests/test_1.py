from scripts.counter import addder

def test_addder_integer():
    assert addder(5) == True

def test_addder_string():
    assert addder("koala") == False

def test_addder_float():
    assert addder(2.5) == False

def test_addder_float():
    assert addder(3.5) != True

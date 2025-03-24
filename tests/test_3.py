from scripts.counter import addder

def test_addder_integer():
    assert addder(11) == 21

def test_addder_string():
    assert addder("koala") == False

def test_addder_float_1():
    assert addder(2.5) == False
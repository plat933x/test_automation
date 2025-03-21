from scripts import counter

def test_addder_integer():
    assert addder(5) == True

def test_addder_string():
    assert addder("koala") == False

def test_addder_float_1():
    assert addder(2.5) == False

def test_addder_float_2():
    assert addder(3.5) != True

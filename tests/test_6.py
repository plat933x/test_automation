''' simple operations on lists'''

list_1 = [12,5,-3,0,-6,7,8,4]

def test_max():
    assert max(list_1) == 12

def test_min():
    assert min(list_1) == -6

def test_start():
    assert list_1[0] == 12

def test_end():
    assert list_1[-1] == 4

def test_new_end():
    list_1.append(17)
    assert not list_1[-1] == 4
    assert list_1[-1] == 17
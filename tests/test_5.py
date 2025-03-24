def simple_calc(a,b,n):
    if n == "*":
        return a*b
    elif n == '/':
        return a/b
    elif n == '+':
        return a+b
    elif n == '-':
        return a-b


def test_product():
    assert simple_calc(12,3,"*") == 36

def test_divide():
    assert simple_calc(100,10,"/") == 10

def test_add():
    assert simple_calc(17.5, 0.25, "+") == 17.75

def test_subtract():
    assert simple_calc(2, 14, "-") == -12
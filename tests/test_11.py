'''shopping discount adder'''

def discount_adder(price,discount):
    return price*(1-discount/100)

def test_discount_1():
    assert discount_adder(149.99, 5) < 149.99

def test_discount_2():
    assert discount_adder(149.99,0) == 149.99
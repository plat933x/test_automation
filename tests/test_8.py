from scripts.car_brand_check import *

def test_volvo():
    assert is_car_brand_german("Volvo") != True

def test_volkswagen():
    assert is_car_brand_german("VW") == True

def test_fiat():
    assert is_car_brand_german("Fiat") == False

def test_benz():
    assert is_car_brand_german("Mercedes")
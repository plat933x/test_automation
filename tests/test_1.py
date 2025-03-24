from scripts.cred_card_hider import credit_num_hidden
from scripts.decimal_to_binary import decimal_to_binary
from scripts.vowel_counter import *

def test_credit_card_positive():
    assert credit_num_hidden("4850215963219669")[0:5] == "*****"
    assert credit_num_hidden("4850215963219669")[-4:] == "9669"

def test_credit_card_negative():
    assert not credit_num_hidden("4850215963219669")[0:5] == "48502"
    assert not credit_num_hidden("4850215963219669")[-4:] == "****"

def test_decimal_to_binary_positive():
    assert decimal_to_binary(27) == '11011 '

def test_decimal_to_binary_negative():
    assert decimal_to_binary(5) != "1111"

def test_vowel_counter_positive():
    assert vowel_counter("counter") == 3
    assert vowel_counter("mitsubishi") == 4

def test_vowel_counter_negative():
    assert vowel_counter("audi") != 5
    assert not vowel_counter("bmw") == 1

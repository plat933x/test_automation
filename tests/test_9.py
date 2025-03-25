'''counting occurrence of letter in a word'''

def letters_counter(word, letter):
    counter = 0
    for i in range(len(word)):
        if word[i] == letter.upper() or word[i] == letter.lower():
            counter += 1
    return counter


def test_letters_counter_1():
    assert letters_counter("Warszawa", "W") == 2

def test_letters_counter_2():
    assert letters_counter("500589897", "8") > 1
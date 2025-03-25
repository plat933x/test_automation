'''check if words are anagrams'''

def are_anagrams(word1,word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def test_are_anagrams_1():
    assert are_anagrams("Water", "Cola") == False

def test_are_anagrams_2():
    assert are_anagrams("Puma", "Ampu")
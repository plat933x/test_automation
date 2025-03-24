def vowel_counter(x):

    vowels = ["a","e","i","o","u","y"]
    counter = 0

    for i in x:
        if i in vowels:
            counter += 1
    return counter
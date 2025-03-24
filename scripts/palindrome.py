def palindrome(x):
    x_rev = str(x[::-1])

    for index in x_rev:
        print(index, end='')

    if x == x_rev:
        return True
    else:
        return False
def addder(n):

    if type(n) == str or type(n) == float:
        return False

    prev_number = 0
    for i in range(1,n+1):
        sum = prev_number + i
        print(f"Current index: {i}, prev_number: {i-1}, sum: {sum}")
        prev_number = i
    return sum
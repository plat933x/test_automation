'''Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with
an asterisk except the last four. For example, if the function gets sent “4444444444444444”, then it should return “4444”.'''

def credit_num_hidden(credit_card):
    if not isinstance(credit_card, str) or len(credit_card) < 4:
        raise ValueError("Provide string and length must be greater than 4 signs")
    return '*' * (len(credit_card) - 4) + credit_card[-4:]

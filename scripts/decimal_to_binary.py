def decimal_to_binary(n):
    """Converts a decimal number to binary."""
    if n == 0:
        return "0"
    binary = " "
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

print(decimal_to_binary(27))
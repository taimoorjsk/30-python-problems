# Problem: Digital Power (DigPow)
# For a number n and power p, compute the sum of each digit raised to
# consecutive powers (p, p+1, p+2, ...). Return the result divided by n
# if evenly divisible; otherwise return -1.

def dig_pow(n, p):
    total = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))

    return total // n if total % n == 0 else -1

# Examples:
print(dig_pow(695, 2))    # Output: 2
print(dig_pow(46288, 3))  # Output: 51
print(dig_pow(92, 1))     # Output: -1

# Problem: Prime Number Check
# Determine whether a given positive integer is a prime number —
# divisible only by 1 and itself.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Examples:
print(is_prime(2))   # Output: True
print(is_prime(15))  # Output: False
print(is_prime(29))  # Output: True

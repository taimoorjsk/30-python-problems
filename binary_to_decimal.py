# Problem: Binary to Decimal
# Convert a binary string (e.g. "1011") into its decimal integer equivalent.

def binary_to_decimal(binary):
    decimal = 0

    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            decimal += 2 ** i

    return decimal

# Examples:
print(binary_to_decimal("1011"))  # Output: 11
print(binary_to_decimal("1111"))  # Output: 15
print(binary_to_decimal("10000")) # Output: 16

# Problem: Second Largest Number
# Find the second largest distinct value in a list of numbers.
# Return None if fewer than two distinct values exist.

def second_largest(numbers):
    unique = sorted(set(numbers), reverse=True)

    if len(unique) < 2:
        return None

    return unique[1]

# Examples:
print(second_largest([10, 5, 8, 10, 3]))  # Output: 8
print(second_largest([7, 7, 7]))            # Output: None
print(second_largest([1, 2]))               # Output: 1

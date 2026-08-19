# Problem: Fibonacci Sequence
# Generate the first n numbers of the Fibonacci sequence, where each
# number is the sum of the two preceding ones (starting with 0 and 1).

def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]

    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]

# Examples:
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(1))  # Output: [0]
print(fibonacci(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

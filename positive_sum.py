# Problem: Positive Sum
# Return the sum of all positive numbers in an array.
# Negative numbers and zero are ignored.

def positive_sum(arr):
    return sum(n * (n > 0) for n in arr)

# Example usage:
print(positive_sum([1, -4, 7, 12]))
print(positive_sum([-1, -2, -3]))
print(positive_sum([]))

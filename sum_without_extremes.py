# Problem: Sum Without Extremes
# Return the sum of all array elements except the highest and lowest values.
# If the array has fewer than 3 elements, return 0.

def sum_array(arr):
    return sum(sorted(arr or [])[1:-1])

# Examples:
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([5, 2]))
print(sum_array([]))

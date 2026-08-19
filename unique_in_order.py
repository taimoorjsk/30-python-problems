# Problem: Unique In Order
# Remove consecutive duplicate elements from a sequence while preserving
# the original order. Non-consecutive duplicates are kept.

def unique_in_order(sequence):
    result = []

    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)

    return result

print(unique_in_order('AAAABBBCCDAABBB')) # Output: ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))         # Output: ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3]))   # Output: [1, 2, 3]
print(unique_in_order(''))                # Output: []

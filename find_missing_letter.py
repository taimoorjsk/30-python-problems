# Problem: Find Missing Letter
# Given a list of consecutive letters (with one missing), return the
# letter that completes the sequence.

def find_missing_letter(chars):
    for i in range(1, len(chars)):
        current = ord(chars[i - 1])
        nxt = ord(chars[i])

        if nxt - current > 1:
            return chr(current + 1)

    return ""

# Examples:
print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))   # Output: 'e'
print(find_missing_letter(['O', 'Q', 'R', 'S']))        # Output: 'P'
print(find_missing_letter(['w', 'x', 'y', 'z']))        # Output: ''

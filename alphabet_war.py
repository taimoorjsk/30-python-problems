# Problem: Alphabet War
# Two armies face off: left (w, p, b, s) vs right (m, q, d, z), each with
# different power values. Priests (t, j) adjacent to enemies convert them.
# Determine which side wins based on total remaining power.

def alphabet_war(fight):
    left_powers = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_powers = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    to_left = {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's'}
    to_right = {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z'}

    final_chars = list(fight)
    n = len(fight)

    for i in range(n):
        char = fight[i]

        has_t = False
        has_j = False

        if i > 0:
            if fight[i-1] == 't': has_t = True
            if fight[i-1] == 'j': has_j = True

        if i < n - 1:
            if fight[i+1] == 't': has_t = True
            if fight[i+1] == 'j': has_j = True

        if has_t and not has_j:
            final_chars[i] = to_left.get(char, char)
        elif has_j and not has_t:
            final_chars[i] = to_right.get(char, char)

    left_score = 0
    right_score = 0

    for char in final_chars:
        if char in left_powers:
            left_score += left_powers[char]
        elif char in right_powers:
            right_score += right_powers[char]

    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"

# Examples:
print(alphabet_war("z"))    # Output: "Right side wins!"
print(alphabet_war("tz"))   # Output: "Left side wins!"
print(alphabet_war("jz"))   # Output: "Right side wins!"
print(alphabet_war("ztj"))  # Output: "Left side wins!"

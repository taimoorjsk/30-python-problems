# Problem: Middle Character(s)
# Return the middle character of a string. If the string length is odd,
# return one character; if even, return the two middle characters.

def get_middle(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]

# Examples:
print(get_middle("test"))     # Output: "es"
print(get_middle("testing"))  # Output: "t"
print(get_middle("A"))        # Output: "A"

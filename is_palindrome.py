# Problem: Palindrome Checker
# Determine whether a given string reads the same forwards and backwards.
# Ignore case and non-alphanumeric characters when checking.

def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# Examples:
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))                        # Output: False
print(is_palindrome("Noon"))                              # Output: True

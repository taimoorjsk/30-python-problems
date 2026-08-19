# Problem: Anagram Check
# Determine whether two strings are anagrams — they contain the same
# characters in the same frequency, ignoring case and spaces.

def are_anagrams(first, second):
    normalize = lambda text: sorted(char.lower() for char in text if char.isalpha())
    return normalize(first) == normalize(second)

# Examples:
print(are_anagrams("listen", "silent"))     # Output: True
print(are_anagrams("hello", "bello"))       # Output: False
print(are_anagrams("Dormitory", "Dirty room"))  # Output: True

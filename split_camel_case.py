# Problem: Split Camel Case
# Insert a space before each uppercase letter in a camelCase string,
# effectively separating words while preserving the original casing.

import re

def solution(s):
    return re.sub(r"([A-Z])", r" \1", s)

# Examples:
print(solution("camelCasing")) # Output: "camel Casing"
print(solution("identifier"))  # Output: "identifier"
print(solution(""))            # Output: ""

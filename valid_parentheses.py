# Problem: Valid Parentheses
# Given a string containing only '(' and ')', determine if the parentheses
# are balanced — every opening bracket has a corresponding closing bracket
# in the correct order.

def valid_parentheses(string):
    count = 0

    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            return False

    return count == 0

# Examples:
print(valid_parentheses("()"))             # Output: True
print(valid_parentheses(")(()))"))         # Output: False
print(valid_parentheses("("))              # Output: False
print(valid_parentheses("(())((()())())")) # Output: True

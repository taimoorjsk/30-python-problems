# Problem: Validate ATM PIN
# Check whether a given PIN is valid: it must be exactly 4 or 6 digits long
# and contain only numeric characters.

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# Examples:
print(validate_pin("1234"))   # Output: True
print(validate_pin("12345"))  # Output: False
print(validate_pin("a234"))   # Output: False
print(validate_pin("-123"))   # Output: False

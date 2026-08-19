# Problem: Caesar Cipher
# Encrypt a message by shifting each letter forward by a given number of
# positions in the alphabet. Non-alphabetic characters remain unchanged.

def caesar_cipher(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)

# Examples:
print(caesar_cipher("Hello, World!", 3))  # Output: "Khoor, Zruog!"
print(caesar_cipher("ABC xyz", 1))        # Output: "BCD yza"

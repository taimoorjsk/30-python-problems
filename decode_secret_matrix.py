# Problem: Decode Secret Matrix
# Read a matrix column by column (top to bottom) to reveal a hidden message.
# Replace non-alphanumeric separators between characters with a single space.

import re

def decode_matrix(n, m, matrix):
    decoded_string = "".join([char for col in zip(*matrix) for char in col])

    final_string = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded_string)

    return final_string

if __name__ == "__main__":
    n, m = 7, 3
    matrix = [
        "Tsi",
        "h%x",
        "i #",
        "sM ",
        "$a ",
        "#t%",
        "ir!"
    ]

    print(decode_matrix(n, m, matrix))

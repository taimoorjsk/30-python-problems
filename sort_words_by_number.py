# Problem: Sort Words by Embedded Number
# Given a sentence where each word contains a single digit, reorder the
# words so they appear in ascending order based on that embedded number.

def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()

    sorted_words = sorted(words, key=lambda word: next(char for char in word if char.isdigit()))

    return " ".join(sorted_words)

# Examples:
print(order("is2 Thi1s T4est 3a"))
# Output: "Thi1s is2 3a T4est"

print(order("4of Fo1r pe6ople g3ood th5e the2"))
# Output: "Fo1r the2 g3ood 4of th5e pe6ople"

print(order(""))
# Output: ""

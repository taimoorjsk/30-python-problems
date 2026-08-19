# Problem: Word Frequency Counter
# Count how many times each word appears in a sentence and return
# the results as a dictionary mapping words to their frequencies.

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        cleaned = "".join(char for char in word if char.isalnum())
        if cleaned:
            frequency[cleaned] = frequency.get(cleaned, 0) + 1

    return frequency

# Examples:
print(word_frequency("To be or not to be"))
# Output: {'to': 2, 'be': 2, 'or': 1, 'not': 1}

print(word_frequency("Hello hello HELLO world"))
# Output: {'hello': 3, 'world': 1}

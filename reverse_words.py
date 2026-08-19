# Problem: Reverse Words in a String
# Reverse each individual word in a sentence while preserving word order
# and the original spacing between words.

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

# Examples:
print(reverse_words("This is an example!")) # Output: "sihT si na !elpmaxe"
print(reverse_words("double  spaces"))      # Output: "elbuod  secaps"

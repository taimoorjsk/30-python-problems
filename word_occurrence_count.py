# Problem: Word Occurrence Count
# Read a list of words from user input, then display the count of unique
# words and the occurrence count of each distinct word in order of first appearance.

wordCount = int(input("Enter the number of words: "))
wordlist = []

while wordCount != 0:
    word = str(input("Enter word: "))
    wordlist.append(word)
    wordCount -= 1

print("input List: ", wordlist)

uniqueWords = len(set(wordlist))
print("Number of unique words: ", uniqueWords)
print("Number of occurrences for each distinct word according to their appearance in the input.")

seen = set()
for n in wordlist:
    if n not in seen:
        print(wordlist.count(n), end=" ")
        seen.add(n)

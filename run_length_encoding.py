# Problem: Run-Length Encoding
# Given a word, output the run-length encoding as (count, character) pairs
# for each group of consecutive identical characters.

word = str(input("enter word: "))
previous = word[0]
count = 1
for char in word[1:]:
    if char == previous:
        count += 1
    else:
        print(f"({count}, {previous})", end=" ")
        previous = char
        count = 1
print(f"({count}, {previous})")

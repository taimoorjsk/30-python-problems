# Problem: Separate Integer Digits
# Given an integer, extract and print each digit on a separate line,
# starting from the least significant (rightmost) digit.

num = int(input("Enter an integer to separate: "))

while num != 0:
    digit = num % 10
    num = num // 10
    print(digit)

# Problem: Number Triangle Pattern
# Given a number n, print a triangle where row i contains the digit i
# repeated i times (e.g., row 1 prints "1", row 2 prints "22", etc.).

num = int(input("enter number: "))
for i in range(1, num):
    print(str(i) * i)

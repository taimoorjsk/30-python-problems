# Problem: FizzBuzz
# Print numbers from 1 to n. For multiples of 3 print "Fizz", for multiples
# of 5 print "Buzz", and for multiples of both print "FizzBuzz".

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
fizzbuzz(15)

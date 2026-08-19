# Problem: Longest Consecutive String Concatenation
# Given an array of strings and an integer k, find the longest string formed
# by concatenating k consecutive elements from the array.

def longest_consec(strarr, k):
    n = len(strarr)

    if n == 0 or k > n or k <= 0:
        return ""

    longest = ""

    for i in range(n - k + 1):
        current_str = "".join(strarr[i:i+k])

        if len(current_str) > len(longest):
            longest = current_str

    return longest

# Example usage:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
print(longest_consec(strarr, 2))  # Output: "folingtrashy"

# 30 Python Programming Problems

A collection of 30 Python solutions covering string manipulation, array processing, validation logic, cryptography, number theory, pattern generation, and interactive programs.

---

## Problem Index

| # | File | Problem | Category | Concepts Practiced |
|---|------|---------|----------|-------------------|
| 1 | [`concentric_grid.py`](concentric_grid.py) | **Concentric Grid** — Build an m×n grid where each cell value represents its layer depth from the nearest edge. | Arrays / Patterns | Nested list comprehension, 2D grid indexing, `min()` function, boundary distance logic |
| 2 | [`alphabet_war.py`](alphabet_war.py) | **Alphabet War** — Simulate a battle between two letter armies; priests convert adjacent enemies before power is tallied. | Strings / Logic | Dictionary mapping, adjacent element checks, conditional transformation, score aggregation |
| 3 | [`valid_parentheses.py`](valid_parentheses.py) | **Valid Parentheses** — Determine whether a string of `(` and `)` brackets is properly balanced. | Strings / Validation | Counter-based stack logic, early return, string iteration |
| 4 | [`validate_pin.py`](validate_pin.py) | **Validate ATM PIN** — Check that a PIN is exactly 4 or 6 digits and contains only numbers. | Validation | `str.isdigit()`, length validation, boolean return expressions |
| 5 | [`digital_power.py`](digital_power.py) | **Digital Power** — Sum each digit raised to consecutive powers; return the quotient if divisible by the original number. | Math / Numbers | `enumerate()`, exponentiation, modulo arithmetic, digit extraction via `str()` |
| 6 | [`split_camel_case.py`](split_camel_case.py) | **Split Camel Case** — Insert spaces before uppercase letters to separate camelCase words. | Strings / Regex | Regular expressions, `re.sub()`, capture groups, pattern matching |
| 7 | [`unique_in_order.py`](unique_in_order.py) | **Unique In Order** — Remove consecutive duplicates from a sequence while preserving order. | Arrays / Strings | List building, consecutive element comparison, order-preserving deduplication |
| 8 | [`rock_paper_scissors.py`](rock_paper_scissors.py) | **Rock Paper Scissors** — Play an interactive rock-paper-scissors game against the computer. | Interactive / Games | `input()`, `random.choice()`, conditional branching, input validation |
| 9 | [`sort_words_by_number.py`](sort_words_by_number.py) | **Sort Words by Embedded Number** — Reorder sentence words by the digit embedded in each word. | Strings / Sorting | Custom sort key, lambda functions, `sorted()`, digit extraction |
| 10 | [`longest_consecutive_concat.py`](longest_consecutive_concat.py) | **Longest Consecutive Concatenation** — Find the longest string formed by joining *k* consecutive array elements. | Strings / Arrays | Sliding window, array slicing, string joining, edge-case handling |
| 11 | [`middle_character.py`](middle_character.py) | **Middle Character(s)** — Return the middle character of a string, or both middle characters if length is even. | Strings | String slicing, integer division, length calculation |
| 12 | [`reverse_words.py`](reverse_words.py) | **Reverse Words in a String** — Reverse each word individually while keeping word order and spacing intact. | Strings | List comprehension, slice reversal `[::-1]`, `split()` / `join()` |
| 13 | [`football_points.py`](football_points.py) | **Football Match Points** — Calculate league points from match scores (win = 3, draw = 1, loss = 0). | Arrays / Logic | String splitting, `map()`, tuple unpacking, conditional accumulation |
| 14 | [`sum_without_extremes.py`](sum_without_extremes.py) | **Sum Without Extremes** — Sum all array elements except the highest and lowest values. | Arrays / Math | Sorting, list slicing, handling empty/small arrays with `or []` |
| 15 | [`positive_sum.py`](positive_sum.py) | **Positive Sum** — Return the sum of all positive numbers in an array. | Arrays / Math | Generator expressions, boolean filtering `(n > 0)`, `sum()` aggregation |
| 16 | [`decode_secret_matrix.py`](decode_secret_matrix.py) | **Decode Secret Matrix** — Read a character matrix column-wise to reveal a hidden message. | Strings / Matrix | `zip(*matrix)` transposition, regex substitution, column-wise traversal |
| 17 | [`run_length_encoding.py`](run_length_encoding.py) | **Run-Length Encoding** — Output `(count, character)` pairs for consecutive identical characters in a word. | Strings / Patterns | While/for loops, run tracking, formatted output, user input |
| 18 | [`number_triangle_pattern.py`](number_triangle_pattern.py) | **Number Triangle Pattern** — Print a triangle where row *i* repeats the digit *i* exactly *i* times. | Patterns / Loops | `for` loops, string repetition, pattern printing, user input |
| 19 | [`word_occurrence_count.py`](word_occurrence_count.py) | **Word Occurrence Count** — Count unique words and display each word's frequency in order of first appearance. | Arrays / Counting | Sets, `list.count()`, ordered iteration, user input loops |
| 20 | [`separate_integer_digits.py`](separate_integer_digits.py) | **Separate Integer Digits** — Print each digit of an integer on its own line, from right to left. | Numbers / Loops | Modulo (`%`), integer division (`//`), while loops |
| 21 | [`is_palindrome.py`](is_palindrome.py) | **Palindrome Checker** — Determine whether a string reads the same forwards and backwards, ignoring case and punctuation. | Strings / Validation | String cleaning, slice reversal, `isalnum()`, case normalization |
| 22 | [`fizzbuzz.py`](fizzbuzz.py) | **FizzBuzz** — Print numbers 1 to *n*, replacing multiples of 3 with "Fizz", 5 with "Buzz", and both with "FizzBuzz". | Logic / Loops | Modulo operator, `if/elif/else` chains, `range()` loops |
| 23 | [`find_missing_letter.py`](find_missing_letter.py) | **Find Missing Letter** — Given a list of consecutive letters with one missing, return the letter that completes the sequence. | Strings / Logic | `ord()` / `chr()` conversion, gap detection, list iteration |
| 24 | [`caesar_cipher.py`](caesar_cipher.py) | **Caesar Cipher** — Encrypt a message by shifting each letter forward by a fixed number of positions in the alphabet. | Strings / Cryptography | Character arithmetic, modulo wrapping, `isupper()` / `islower()`, string building |
| 25 | [`binary_to_decimal.py`](binary_to_decimal.py) | **Binary to Decimal** — Convert a binary string into its decimal integer equivalent. | Numbers / Math | Powers of two, `reversed()` iteration, positional notation |
| 26 | [`second_largest.py`](second_largest.py) | **Second Largest Number** — Find the second largest distinct value in a list of numbers. | Arrays / Logic | `set()` for uniqueness, sorting, edge-case handling with `None` |
| 27 | [`anagram_check.py`](anagram_check.py) | **Anagram Check** — Determine whether two strings contain the same characters in the same frequency. | Strings / Logic | Lambda functions, sorted comparison, character normalization |
| 28 | [`fibonacci_sequence.py`](fibonacci_sequence.py) | **Fibonacci Sequence** — Generate the first *n* numbers where each is the sum of the two preceding ones. | Sequences / Math | While loops, list appending, sequence generation, slicing |
| 29 | [`prime_check.py`](prime_check.py) | **Prime Number Check** — Determine whether a positive integer is divisible only by 1 and itself. | Numbers / Math | Divisibility testing, square-root optimization, early return |
| 30 | [`word_frequency.py`](word_frequency.py) | **Word Frequency Counter** — Count how many times each word appears in a sentence using a dictionary. | Strings / Dictionaries | Dictionary `get()` method, frequency counting, string cleaning, case normalization |

---

## How to Run

Each file is self-contained and can be executed directly:

```bash
python concentric_grid.py
python fizzbuzz.py
python rock_paper_scissors.py
```

Interactive programs (`rock_paper_scissors.py`, `run_length_encoding.py`, `number_triangle_pattern.py`, `word_occurrence_count.py`, `separate_integer_digits.py`) prompt for user input at runtime.

---

## Topics Covered

- **String manipulation** — reversal, splitting, validation, encoding, decoding, anagrams, palindromes
- **Array processing** — filtering, sorting, summing, deduplication, sliding windows
- **Logic & algorithms** — bracket matching, grid generation, FizzBuzz, prime checking, Fibonacci
- **Number systems** — binary conversion, digit extraction, modulo arithmetic, exponentiation
- **Cryptography** — Caesar cipher, character shifting
- **Data structures** — dictionaries, sets, nested lists, matrix transposition
- **Regular expressions** — camelCase splitting, matrix message cleanup
- **Interactive I/O** — user input, game logic, pattern display

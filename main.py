#Problem 1: Reverse a String
def reverse_string(s):
    return s[::-1]

# Example
print(reverse_string("hello"))  # Output: "olleh"
# Problem 2: Count Vowels in a String
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# Example
print(count_vowels("Apple"))  # Output: 2

#Problem 3: Sum of Digits

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example
print(sum_of_digits(1234))  # Output: 10

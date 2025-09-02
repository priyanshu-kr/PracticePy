def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for c in s if c in vowels)

print(count_vowels("Hello World"))  # Output: 3
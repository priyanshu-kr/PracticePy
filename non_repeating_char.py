# Non-Repeating Character in a String

def first_non_repeating(s):
    from collections import Counter
    count = Counter(s)
    for c in s:
        if count[c] == 1:
            return c
    return None

print(first_non_repeating("aabbcdee"))
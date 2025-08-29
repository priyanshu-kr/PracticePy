# Through simultaneous unpacking.

def fibonacci(n):
    a, b = 0, 1
    result = []
    while a<= n:
        result.append(a)
        a, b = b,a + b
    return result

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8]

# Through sequential assignment.

def fibonacci_seq(n):
    a = 0
    b = 1
    result = []
    while a<=n:
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fibonacci_seq(10))  # Output: [0, 1, 1, 2, 3, 5, 8]


# Note: The simultaneous unpacking method is more Pythonic and concise, while the sequential assignment method is more explicit and easier to understand for beginners.
# Both methods yield the same result.

# 1. a, b = b, a                       This swaps the values of a and b in one go (simultaneous unpacking).
# 2. temp = a; a = b; b = temp         Here, the first line changes a, so the second line doesn't swap - it makes both equal (sequential assignment).
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(8, 20)) #output 4
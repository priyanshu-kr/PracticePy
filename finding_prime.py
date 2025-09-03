def print_primes(low, high):
    for num in range(low, high + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")

print_primes(10, 20)  # Output: 11 13 17 19

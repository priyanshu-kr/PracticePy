def fun(n):
    i = 1
    if (n>=5): return n
    n = n+i
    i = i+1
    return fun(n)

print(fun(1))
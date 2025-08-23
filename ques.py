def Trial(a, b, c):
    if a>=b and b>c:
        return b
    elif a>=b:
        return Trial(a, c, b)
    else:
        return Trial(b, a, c)
    
# print(Trial(10, 11, 9)) # return middle element
# print(Trial(3, 3, 3))  # Infinite Recursion Error
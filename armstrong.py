def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(d)**power for d in str(num))

<<<<<<< HEAD
print(is_armstrong(153))  # Output: True
=======
print(is_armstrong(153))  # Output: True
>>>>>>> 0941a963c96887f4c1252bb029df5980b4cc2e3f

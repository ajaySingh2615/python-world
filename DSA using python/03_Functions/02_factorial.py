def factorial_algo(a):
    sum = 1
    while a != 0:
        sum *= a
        a -= 1
    return sum


a = 5
print(f"Factorial of {a} is {factorial_algo(a)}")

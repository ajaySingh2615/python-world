import math

num = 6

isPrime = True

for i in range(2, math.isqrt(num) + 1):
    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

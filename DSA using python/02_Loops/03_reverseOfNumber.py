a = 1033

reverse = 0

while a > 0:
    last_digit = a % 10
    reverse = reverse * 10
    reverse = reverse + last_digit
    a = a // 10

print(reverse)

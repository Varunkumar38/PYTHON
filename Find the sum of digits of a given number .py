n = int(input("Enter a number: "))
num = n
sumdigits = 0
while num > 0:
    digit = num % 10
    sumdigits += digit
    num = num // 10
print("Sum of digits of", n, "is", sumdigits)
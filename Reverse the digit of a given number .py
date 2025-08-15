n = int(input("Enter a number: "))
num = n
reversenumber = 0
while num > 0:
    digit = num % 10
    reversenumber = reversenumber * 10 + digit
    num = num // 10
print("Reverse of", n, "is", reversenumber)
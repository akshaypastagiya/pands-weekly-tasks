# collatz.py
# This program is enter integer value
# Calculate the naxt value untill value become 1
# To calculate next value is value is even then devide it by 2 
# if value is odd then multiply it by 3 and add one
# Aurthor: Akshay Pastagiya

number = int(input("Enter an intiger number: "))
numbers = []
while number != 1:
    if (number % 2) == 0:
        number = number / 2
    else:
        number = (number * 3) + 1
    numbers.append(int(number))

print(numbers)
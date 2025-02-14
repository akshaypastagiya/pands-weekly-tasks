#bank.py
#this program to enter the 2 value in cent
#sumup this 2 value
#display value in euro and cent

amount1 = input("Enter amount1 (in cent): ")
amount2 = input("enter amount2 (in cent): ")

total = int(amount1) + int(amount2)

eurovalue = round((int(total)/100),2)

print(f"The sum of these is €{eurovalue}")
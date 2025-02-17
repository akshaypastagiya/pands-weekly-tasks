# accounts.py
# This program is convert and bank account number in to last 4 digit visiable account number only and remaining number convert in to x
# Display converted bank account
# Aurthor: Akshay Pastagiya

accountnumber = input("Please enter an account number : ")
# Get the account number length
accountnumberlength = len(accountnumber)

# If account number lenth is 10 or more then display X based on number of charater
if accountnumberlength > 9:
    # Get last 4 digit of account number
    last4numbers  = accountnumber[accountnumberlength-4:accountnumberlength]
    # Convert remaining number in to "X"
    convertstring = "X" * int(accountnumberlength-4)

# if account number is between 4 to 9 charater the diaplay atleat 10 charater including "X"
elif accountnumberlength > 4 and accountnumberlength < 10:
    # Get last 4 digit of account number
    last4numbers  = accountnumber[accountnumberlength-4:accountnumberlength]
    # Convert remaining number in to "X"
    convertstring = "X" * 6

# If account number is less then 4 charater then add o infront of remaining 4 charater and display 10 charater including added 0s and X
else:
    last4numbers = "0" * int(4-accountnumberlength) + accountnumber
    convertstring = "X" * 6

# Display converted account number
print(f"{convertstring}{last4numbers}")
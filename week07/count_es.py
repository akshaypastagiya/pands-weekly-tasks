# counts_es.py
# This program is to counts the es number contain
# number will be stored in the text file
# number should be intiger
# user will be asked to enter the txt file name with extension
# Aurthor: Akshay Pastagiya

import os.path

# Get file name where number is stored
FILENAME = input(f"Enter the file name which contain the number ")

# Check file name id exist or not
if not(os.path.isfile(FILENAME)):
    print("File Does not Exist")
    print("Please enter correct text file name with extention")

# Open File and read the data in file name
with open(FILENAME) as f:
    data = f.read()

# Check number is negative or not
if data[0:1] == "-":
    numberisnegative = 1
    getnumber = data[1:len(data)]
else:
    numberisnegative = 0
    getnumber = data

# Check number is numeric or not
numberisint = getnumber.isnumeric()

if not numberisint:
    print(f"Number is not an intiger, Please enter correct intiger number in text file {FILENAME}")
elif numberisnegative == 0:
    print(f"number of es of the value {data} is {len(data)-1}")
else:
    print(f"number of es of the value {data} is -{len(getnumber)-1}")
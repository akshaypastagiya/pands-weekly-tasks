# squareroot.py
# This program is to generate square root of positive floting number
# In this program we are not using python in build function
# Aurthor: Akshay Pastagiya


def squareroot(number):
    # intial guess
    intial = number/2
    # How accurate squareroot suppose to be
    tolerance = 0.001
    
    # Create Loop to get square root
    for _ in iter(int,1) :
        # Step1 to get square root
        num1 = (number / intial)  
        # Step1 to get square root      
        num2 = (intial+num1) 
        # Get Square root      
        sqrtnum = num2/2
        
        # Check the number we are getting for square root is within tollerance or not        
        if abs(sqrtnum - intial) < tolerance:
            return sqrtnum
        # Update the guess number for square root
        intial = sqrtnum

# Get number for which require to calculate square root
number = float(input("Please Enter a positive number: "))

# Call square root function to get square root value
sqrt = squareroot(number)

# Dispaly the answer of the square root
print(f"The square root of {number} is approx. {sqrt:.1f}")



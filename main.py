
#Repeat until the numbers are both integers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

while True:
    #If these numbers are very large or very small nothing should change due to the nature of python's floating point variables
    #Check validity of num1 and num2 with try: except:
    try:
        num1 = float(num1)
        num2 = float(num2)
        break
    except:
        print("Both num1 and num2 must be able to be expressed as floating point values. Please try again.")
        continue
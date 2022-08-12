import time
from math import *


print("""


******************************

Welcome to the calculator...

You can find the actions you can take below...

1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Square root
6-X to the power of Y
7-log on base 10
8-log of Y on base X
9-Factorial


0-Exit the program

*******************************
""")

while True:
    action=int(input("Please choose your action:"))

    if action == 0:
        print("Exiting the program...")
        time.sleep(1)
        print("The calculator has been closed... See you later!")
        break

    elif action == 1:

        print("Addition has been chosen")
        a = float(input("Please enter your first number:"))
        b = float(input("Please enter your second number:"))
        print("Calculating...")
        time.sleep(1)
        print("{} + {} = {}".format(a, b, a + b))

    elif action == 2:

        print("Subtraction has been chosen...")
        a = float(input("Please enter the minuend:"))
        b = float(input("Please enter the subtrahend:"))
        print("Calculating...")
        time.sleep(1)
        print("{} - {} = {}".format(a, b, a - b))

    elif action == 3:

        print("Multiplication has been chosen...")
        a=float(input("Please enter the multiplicand:"))
        b=float(input("Please enter the multiplier"))
        print("Calculating...")
        time.sleep(1)
        print("{} x {} = {}".format(a,b,a*b))

    elif action == 4:

        print("Division has been chosen...")
        a = float(input("Please enter the dividend:"))
        b = float(input("Please enter the divisor:"))
        print("Calculating...")
        time.sleep(1)
        print("{} : {} = {}".format(a, b, a / b))

    elif action == 5:
        
        print("Square root has been chosen...")
        a = float(input("Please enter the number you want to square root:"))
        if (a < 0):
            print("Invalid request!")
        else:
            print("Calculating...")
            time.sleep(1)
            print("The square root of {} is {}".format(a, a ** 0.5))

    elif action == 6:
        
        print("Exponentiation has been chosen ...")
        print("Please do not enter a negative power")
        a = float(input("Please enter the base:"))
        b = float(input("Please enter the power:"))
        if (b < 0):
            print("Invalid request!")
        else:
            print("Calculating...")
            time.sleep(1)
            print("{} to the power of {} is {}".format(a, b, pow(a, b)))

    elif action == 7:
        
        print("Logarithm operation in base ten has been chosen...")
        a = float(input("Please enter the number you want to logarithm in base ten:"))
        if (a <= 0):
            print("Invalid request!")
        else:
            print("Calculating...")
            time.sleep(1)
            print("Logarithm {} in base 10 equals {}:".format(a, log10(a)))

    elif action == 8 :
        
        print("Logarithm of Y in base X was chosen...")
        a = float(input("X:"))
        if (a == 0 or a == 1):
            print("Invalid request!")
        b = float(input("Y:"))
        if (b <= 0):
            print("Invalid request!")
        else:
            print("Calculating...")
            time.sleep(1)
            print("Logarithm {} in base {} equals {}:".format(b, a, log(b, a)))

    elif action == 9:
        
        print("Factorial finding has been chosen...")
        a = int(input("Please enter the number you want to get the factorial of:"))
        if (a < 0):
            print("Invalid request!")
        else:
            print("Calculating...")
            time.sleep(1)
            print("Factorial {} = {}".format(a, factorial(a)))
    else:
        print("Invalid request! Please select a valid action.")

     
     
  
  
          

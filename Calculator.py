from math import*
from time import sleep

print("""


******************************

Welcome to the calculator...

You can find the actions you can take below...

İşlemler;

1-Addition
2-Substraction
3-Multiplication
4-Division
5-Square root
6-X to the power of Y
7-log on base 10
8-log of X on base Y
9-Factorial


0-Exit the program

*******************************
""")

while True:
    action=int(input("Please choose your action:"))
    if action ==0:
        print("Exitting the program...")
        sleep(1)
        print("The calculator has been closed... See you later!")
        break
        
    elif(action==1):
        print("Addition has been chosen")
        a=float(input("Please enter your first number:"))
        b=float(input("Please enter your second number:"))
        print("Calculating...")
        sleep(1)
        print("{} + {} = {}:".format(a,b,a+b))
    elif(action==2):
        print("Subtraction has been chosen...")
        a=float(input("Please enter the minuend:"))
        b=float(input("Please enter the subtrahend:"))
        print("Calculating...")
        sleep(1)
        print("{} - {} = {}".format(a,b,a-b))

  
  
          

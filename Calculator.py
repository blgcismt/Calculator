from math import*
from time import sleep


print("""


Welcome to the calculator....

You can find the actions you can take below;
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square root
6. X to the power Y
7. log on base 10
8. log of X on base Y
9. Factorial

0. Exit the program

""")


while True:
  action = int(input("Please choose your action:"))
  
  if action == 0 :
    print("Exitting the program...)
    sleep(1)
    print("The prgoram has been closed... See you later!")

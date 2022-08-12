import time
import random
import math


class Computer:
    def __init__(self, status="Off", os=["macOS"], model="Macbook Pro",
                 applications=["Safari", "Spotify", "Discord", "Steam", "Pycharm", "Netbeans"]):

        self.status = status
        self.os = os
        self.model = model
        self.applications = applications

    def open_pc(self):

        if self.status == "Off":
            print("Booting up...")
            time.sleep(1)
            self.status = "On"
            print("Your computer is turned on...")

        elif self.status == "On":
            print("The computer is already on...")

    def close_pc(self):

        if self.status == "On":
            print("Turning off your computer...")
            time.sleep(1)
            self.status = "Off"
            print("Your computer has been shut down...")

        elif self.status == "Off":
            print("The computer is already off.")

    def calculator(self):

        if self.status == "On":
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
                action = int(input("Please choose your action:"))

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
                    a = float(input("Please enter the multiplicand:"))
                    b = float(input("Please enter the multiplier"))
                    print("Calculating...")
                    time.sleep(1)
                    print("{} x {} = {}".format(a, b, a * b))

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

                elif action == 8:

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
        elif self.status == "Off":
            print("Computer is turned off, please open it to access the calculator...")

    def guessing_game(self):
        
        if self.status == "On":
            print(""" 
            Welcome to the Number Guessing Game!
            Guess the number between 1 and 1000....
            You have 10 guesses....
            """)

            random_number = random.randint(1, 1000)
            guesses = 10

            while True:

                guess = int(input("Please enter your guess:"))

                if guess < random_number:
                    print("Checking your number...")
                    time.sleep(1)
                    print("Please enter a bigger number...")
                    guesses -= 1
                    print("Number of guesses left : ", guesses)

                elif guess > random_number:
                    print("Checking your number...")
                    time.sleep(1)
                    print("Please enter a smaller number...")
                    guesses -= 1
                    print("Number of guesses left : ", guesses)

                else:
                    print("Checking your number...")
                    time.sleep(1)
                    print("Congratulations, your answer is correct! Your number is:", random_number)
                    break

                if guesses == 0:
                    print("You're out of guesses, you've lost the game!")
                    break
                    
        elif self.status == "Off":
            print("Computer is turned off, please open it to access the number guessing game...")
      
      def __str__(self):
            
        return """
        
        Computer Specs:
        
        Applications: {}
        Model: {}
        Status: {}
        OS: {}
        
        """.format(self.applications,self.model,self.status,self.os)
        
 
      def remove_os(self):
        if self.status == "On":
            if len(self.os) == 1:
                print("Your OS : {}".format(self.OS[0]))
                action = input("Would you like to remove your operating system?(Y/N)")

                if action == "Y":
                    print("{} is being removed from your computer please wait...".format(self.OS[0]))
                    time.sleep(3)
                    self.os.pop(0)
                    print("Your current operating system has been uninstalled you can select 'Install operating system' for a new operating system.")
                elif action == "N":
                    print("Exiting")
                    time.sleep(1)
                    print("OS removing process has been exited...")
                else:
                    print("Invalid request!")
            else:
                print("Computer does not have any operating system")
        elif self.status == "Off":
            print("Computer is off, please turn it on to access this service...")

        
            

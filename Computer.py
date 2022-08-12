import time
import random
import math
import datetime
import calendar


class Computer:
    def __init__(self, status="Off", os=["macOS"], model="Macbook Pro",
                 applications=["""Safari", "Spotify", "Discord", "Steam", "Pycharm", "Netbeans","Zoom",
                 "Adobe Acrobat Reader DC","Microsoft Word","Microsoft Excel","Microsoft PowerPoint","Photos"""]):

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
                        print("Logarithm {} in base 10 equals {}:".format(a, math.log10(a)))

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
                        print("Logarithm {} in base {} equals {}:".format(b, a, math.log(b, a)))

                elif action == 9:

                    print("Factorial finding has been chosen...")
                    a = int(input("Please enter the number you want to get the factorial of:"))
                    if (a < 0):
                        print("Invalid request!")
                    else:
                        print("Calculating...")
                        time.sleep(1)
                        print("Factorial {} = {}".format(a, math.factorial(a)))
                else:
                    print("Invalid request! Please select a valid action.")
        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")

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
            print("Computer is turned off, please turn it on to access this service...")

    def __str__(self):

        return """

        Computer Specs:

        Applications: {}
        Model: {}
        Status: {}
        OS: {}

        """.format(self.applications, self.model, self.status, self.os)

    def remove_os(self):
        if self.status == "On":
            if len(self.os) == 1:
                print("Your OS : {}".format(self.os[0]))
                action = input("Would you like to remove your operating system?(Y/N)")

                if action == "Y":
                    print("{} is being removed from your computer please wait...".format(self.os[0]))
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
            print("Computer is turned off, please turn it on to access this service...")

    def download_os(self):
        if self.status == "On":
            if self.os == list():
                answer = input("You currently do not have an operating system. Would you like to download one?(Y/N)")
                if answer == "Y":
                    operating_systems = ["Microsoft Windows","macOS","Linux"]
                    counter = 1
                    for x in operating_systems:
                        print("{}- {}".format(counter,x))
                        counter += 1
                    action = int(input("Please enter the number of the OS you want to install..."))

                    if action == 1:
                        print("{} is being installed,please wait".format(operating_systems[0]))
                        time.sleep(3)
                        self.os.append("Microsoft Windows")
                        print("Your installment has been successfully completed... Your operating system now is: {}".format(self.os[0]))

                    elif action == 2:
                        print("{} is being installed,please wait".format(operating_systems[1]))
                        time.sleep(3)
                        self.os.append("macOS")
                        print("Your installment has been successfully completed... Your operating system now is: {}".format(self.os[0]))
                    elif action == 3:
                        print("{} is being installed,please wait".format(operating_systems[2]))
                        time.sleep(3)
                        self.os.append("Linux")
                        print("Your installment has been successfully completed... Your operating system now is: {}".format(self.os[0]))
            elif len(self.os)>0:
                print("You already have an operating system, you  need to uninstall your current one to install a new one")
                print("Exiting Program...")
                time.sleep(1)
                print("OS installing process has been exited...")

        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")

    def show_specs(self):
        if self.status == "On":
            print("Computer Specs: \nApplications: {}\nModel: {}\nOS: {}\nStatus:{}\n".format(self.applications,self.model,self.os,self.status))
        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")
            
            
            
    def show_date(self):
        if self.status == "On":
            time = datetime.datetime.now()
            print("Current date and time :")
            print(time.strftime("%Y-%m-%d %H:%M:%S"))
        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")
            
            
    def show_calendar(self):
        if self.status == "On":
            year = int(input("Please enter the year:"))
            print(""" Please enter the month in this format:
             eg. 01- January, 02- February, 03- March 04- April, 05- May, 06- June, 07- July, 08- August, 09- September, 10- October, 11- November, 12- December""")
            month = int(input("Please enter the month:"))
            print(calendar.month(year,month))
        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")
    def delete_app(self):
        if self.status == "On":
            choice = input("Would you like to delete an application?(Y/N)")

            if choice == "Y":
                counter = 1
                for x in self.applications:
                    print("{}- {}".format(counter,x))
                    counter +=1
                action = int(input("Enter the number of the application you would like to delete..."))
                print("Deleting the application...")
                self.applications.pop(action-1)
                time.sleep(3)
                print("The application has been deleted...")
                print(self.applications)

            if choice == "N":
                print("Exiting...")
                print("Application deleting process has been exited...")
        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")

    def download_app(self):
        if self.status == "On":
            choice = input("Would you like to download an application?(Y/N)")

            if choice == "Y":
                app = input("Please enter the name of the application you would like to install...")
                print("Installing the application...")
                self.applications.append(app)
                time.sleep(3)
                print("The application has been successfully installed...")
                print(self.applications)
            elif choice == "N":
                print("Exiting...")
                print("Application downloading process has been exited...")

        elif self.status == "Off":
            print("Computer is turned off, please turn it on to access this service...")
            

pc = Computer()

print(""" 

Actions you can take;

1- Access the calculator
2- Get specs
3- Install an OS
4- Delete your OS
5- Number guessing game
6- Turn on the computer
7- Turn off the computer
8- Show date and time
9- Open calendar
10- Download an application
11- Delete an application


0- Exit the code

""")


while True:
    answer = int(input("Please choose an action:"))

    if answer == 1:
        pc.calculator()

    elif answer == 2:
        pc.show_specs()

    elif answer == 3:
        pc.download_os()

    elif answer == 4:
        pc.remove_os()

    elif answer == 5:
        pc.guessing_game()

    elif answer == 6:
        pc.open_pc()

    elif answer == 7:
        pc.close_pc()
        
    elif answer == 8:
        pc.show_date()
    
    elif answer == 9:
        pc.show_calendar()
        
    elif answer == 10:
        pc.download_app()

    elif answer == 11:
        pc.delete_app()

    elif answer == 0:
        print("Exiting the code...")
        break

    else:
        print("Invalid request...")
        
            

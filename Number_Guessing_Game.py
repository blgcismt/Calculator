import time
import random

print(""" 

Welcome to the Number Guessing Game!

Guess the number between 1 and 1000....

You have 10 guesses....

""")

random_number = random.randint(1,1000)
guesses = 10

while True :
  
  guess = int(input("Please enter your guess:"))
  
  if guess < random_number :
    print("Checking your number...")
    time.sleep(1)
    print("Please enter a bigger number...")
    guesses -=1
    print("Number of guesses left : ",guesses)
    
  elif guess > random_number :
    print("Checking your number...")
    time.sleep(1)
    print("Please enter a smaller number...")
    guesses -=1
    print("Number of guesses left : ",guesses)
    
  else:
    print("Checking your number...")
    time.sleep(1)
    print("Congratulations, your answer is correct! Your number is:",random_number)
    break
    
  if guesses == 0 :
    print("You're out of guesses, you've lost the game!")
    break
  
     
    
 
    
     

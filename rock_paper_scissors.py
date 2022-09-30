import random

moves = ["Rock", "Paper", "Scissors"]


computer = moves[random.randint(0,2)]


player = False

scorep = 0
scorec = 0

while player == False:

    player = input("Rock, Paper, Scissors?")
    if scorec == 3:
        print("You lose! Better luck next time...")
        break
    if scorep == 3:
        print("Computer you suck! You lose! Let's go humanity!")
        break
    if player == computer:
        print("Tie!")
        print("Player: " + str(scorep) + " Computer: " + str(scorec))
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            scorec += 1
            print("Player: " + str(scorep) + " Computer: " + str(scorec))
        else:
            print("You win!", player, "smashes", computer)
            scorep += 1
            print("Player: " + str(scorep) + " Computer: " + str(scorec))
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            scorec += 1
            print("Player: " + str(scorep) + " Computer: " + str(scorec))
        else:
            print("You win!", player, "covers", computer)
            scorep += 1
            print("Player: " + str(scorep) + " Computer: " + str(scorec))
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            scorec += 1
            print("Player: " + str(scorep) + " Computer: " + str(scorec))
        else:
            print("You win!", player, "cut", computer)
            scorep += 1
            print("Player: " + str(scorep) + " Computer: " + str(scorec))
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = moves[random.randint(0,2)]

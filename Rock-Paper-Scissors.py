import random

humanWins = 0 
computerWins = 0

options = ["rock", "paper", "scissors"]

while True:
    choice = input("Rock, Paper, or Scissors? Press Q to quit. ").lower()
    if choice == "q":
        break
    
    if choice not in options:
        print("Invalid Entry!")
        continue
    
    randomNum = random.randint(0, 2) # rock: 0, paper: 1, scissors: 2
    computerChoice = options[randomNum]
    print("Computer chose", computerChoice + ".")
    
    if choice == "rock" and computerChoice == "scissors":
        print("You won!")
        humanWins += 1
    
    elif choice == "paper" and computerChoice == "rock":
        print("You won!")
        humanWins += 1
    
    elif choice == "scissors" and computerChoice == "paper":
        print("You won!")
        humanWins += 1
    
    elif choice == computerChoice:
        print("Tie!")
    
    else:
        print("You lost!")
        computerWins += 1
    
print("You won", humanWins, "times")
print("Computer won", computerWins, "times")
print("Goodbye!")
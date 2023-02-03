import random

range = input("Input a number: ")

if range.isdigit():
    range = int(range)
    
    if range <= 0:
        print('Number must be higher than 0!')
        quit()
else:
    print ('Invalid Entry! Must be a number!')
    quit()

number = random.randrange(range)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess a number between 0 - " + str(range) + " ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Invalid entry!')
        continue

    if guess == number:
        print('You guessed it! :)')
        break
    elif guess > number:
        print("Try again, go lower...")
    else:
        print("Try again, go higher...")
        
print("It took you", guesses, "guesses")
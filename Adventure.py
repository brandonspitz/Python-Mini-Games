import random

name = input("What is your name? ")
print("Welcome to Egypt", name)

answer1 = input("While on an exotic vacation, you hear a strange noise coming for the desert. Do you investigate? (Yes or No) ").lower()

if answer1 == "yes":
    answer2 = input("You hear whispers, but you cannot identify where they are coming from and a sandstorm is settling in. Go left or right? ").lower()
    if answer2 == "right":
        answer3 = input("You come across an entrance to an ancient temple. Inside, there are three paths to follow. Do you go left, right, or straight? ").lower()
        if answer3 == "left":
            answer4 = input("You find yourself in a pitch-black maze, yet the whispers get louder. Investigate? (Yes or No) ").lower()
            if answer4 == "no":
                answer5 = input("A dim light guides you away from the whispers. You stumble across a a glowing golden idol. Take it? (Yes or No) ").lower()
                if answer5 == "yes":
                    print("As you lift up your treasure, a booby trap activates and the ceiling slowly descends upon you until you are crushed. You Lose.")
                else:
                    print("As you attempt to retrace your steps, the whispers return and you are pulled away into the dark. You Lose.")
            else:
                print("The noise overwhelms you as you feel hands pull you deeper into the abyss. You Lose.")
        elif answer3 == "right":
            print("A snake-infested pit of sharp spikes appears under the brittle ground you walk across. You Lose.")
        else:
            print('You find the remains of an explorer that came before you. He is carrying a key and a note that reads: "Check behind"')
            answer6 = input("You make your way back, but you find yourself lost in a dark maze. The whispers grow louder. Investigate? (Yes or No) ").lower()
            if answer6 == "no":
                answer7 = input("A dim light guides you away from the whispers. You stumble across a a glowing golden idol. Remembering the note, you check behind the pedestal and find a keyhole. Use your key? (Yes or No) ").lower()
                if answer7 == "yes":
                    answer8 = input("You hear a click followed by silence. You take the idol and bolt towards the exit. You hear the whispers catching up behind you. Turn around and look? (Yes or No) ").lower()
                    if answer8 == "no":
                        print("You narrowly escape with your life and the treasure! You Win", name + "!")
                    else:
                        print("You turn around and an abomination with mouths all over its slender body grabs you... You Lose.")
                else:
                    print("As you lift up your treasure, a booby trap activates and the ceiling slowly descends upon you until you are crushed. You Lose.")
            else:
                print("The noise overwhelms you as you feel hands pull you deeper into the abyss. You Lose.")
    else:
        print("You wander for miles and find yourself hopelessly lost. You Lose.")
else:
    print("You ignored the call to adventure :( You Lose.")
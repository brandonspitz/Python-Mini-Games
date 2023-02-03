print("Welcome to my history quiz!")

play = input("Ready to start? ")

if play.lower() != "yes":
    print(":(")
    quit()

print("Alright! Let's start")

count = 0

answer = input("1. What is the oldest recorded religion in the world? ")
if answer.lower() == "zoroastrianism":
    print('Correct! While few religions claim date back to the start of human history, Zoroastrianism is the first recorded (So far!)')
    count += 1
else:
    print('Incorrect :(')

answer = input("2. What extinct human sub-species dominated what is now Europe thousands of years ago? ")
if answer.lower() == "neanderthals":
    print('Correct! The skeletons of the short and stocky Neanderthals have been found all over the area!')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("3. What art style was popular with the ancient Roman Empire? ")
if answer.lower() == "mosaic":
    print('Correct! Mosiac tile art was commonly used on the walls and floors of Roman architecture')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("4. Which ancient civilization previously inhabited the area now known as Phoenix, Arizona? ")
if answer.lower() == "hohokam":
    print('Correct! The Hohokam people were spread out across the Arizona Southwest')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("5. This ancient dynasty unified China under imperialist rule. ")
if answer.lower() == "qin":
    print('Correct! The Terracota army still stands as a testament to the great rule!')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("6. What was the name of Theodore Roosevelt's famous cavalry unit? ")
if answer.lower() == "rough riders":
    print('Correct! This band of ex-convicts proved to be fierce in the Spanish-American War')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("7. What myth seems to be prevelant in many ancient religions' genisis stories? ")
if answer.lower() == "flood":
    print('Correct! Flood myths can be seen in many European, Asian, and African religions')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("8. This English Explorer was the third to ever circumnavigate the world! ")
if answer.lower() == "sir francis drake":
    print('Correct! Sir Francis was an experienced sailor and privateer tasked with such a grueling adventure')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("9. Which world super power was the first to send a human to space? ")
if answer.lower() == "ussr":
    print('Correct! Not to be confused with just Russia, the USSR sent Yuri Gagarin to space in a crucial moment in the Space Race')
    count += 1
else:
    print('Incorrect :(')
    
answer = input("10. This famous composer made a name for himself despite his inability to hear. ")
if answer.lower() == "beethoven":
    print('Correct! Despite his hearing loss starting in his early-adulthood, Beethoven was an excellent pianist')
    count += 1
else:
    print('Incorrect :(')
    
print("You have completed the test! You're score is " + str(count) + "/10")
print("Or " + str(count / 10 * 100) + "%")
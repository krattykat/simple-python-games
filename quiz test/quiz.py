print("Welcome to my cat quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is a cat's favorite food? ").lower()
if answer == "tuna":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

answer = input("What is a cat's biggest enemy? ").lower()
if answer == "dog":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

answer = input("What is a cat's greatest fear? ").lower()
if answer == "water":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

answer = input("What is the biggest part of a cat? ").lower()
if answer == "their ego":
    print('Correct!')
    score += 1
else:
    print("Incorrect!") 

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/4 * 100) + "%")
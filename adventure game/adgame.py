name = input("Type your name: ")
print(" Welcome", name, "to the adventure!")

answer = input("You are on a dirt road and it has come to an end. You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ")

    if answer == "swim":
        print("You swam across the river, and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked around, ran out of water, and died from dehydration. ")
    else:
        print("Not a valid option. You lsoe.")   

elif answer == "right":
    answer = input("You come to a bridge, it looks unstable. Do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back to the dirt road and lose. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? ")

        if answer == "yes":
            print("The person tells you to walk with them, they'll help you find the way. You win! ")
        elif answer == "no":
            print("He stabs you in the chest and kills you. You lsoe. ")
        else: 
            print("Not a valid option. You lsoe. ")

    else:
        print("Not a valid option. You lsoe.")   

print("Thank you for trying,", name + ".")
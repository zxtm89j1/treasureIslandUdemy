print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your job is to find the treasure! Good luck!")
direction = input('''Let's start your adventure. You're at a crossroad. Where do you want to go? Type "left" or "right"''').lower()

if direction == "right":
    print("You feel into a hole full of alligators! Oh no!")
    print("Game over!")
elif direction == "left":
    action = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across!''').lower()
    if action == "swim":
        print("You are attacked by a trout!")
        print("Game over!")
    elif action == "wait":
        doorColor = input("You arrived at the island unharmed! There is a house with three doors. One red, one yellow and one blue. Which color do you choose?").lower()
        if doorColor == "red":
            print("Burned by fire!")
            print("Game over!")
        elif doorColor == "yellow":
            print("You win! Congratulations!")
        elif doorColor == "blue":
            print("You were eaten by beasts! Sorry!")
            print("Game over!")
        else:
            print("You chose nothing!")
            print("Game over!!!!!!")
    else:
        print("You choose nothing! Sorry!")
        print("Game over!")
else:
    print("You chose nothing! Sorry!")
    print("Game over!")

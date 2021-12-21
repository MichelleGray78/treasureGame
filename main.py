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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

leftOrRight = input("You are at a crossroads, where do you want to go? Type 'left' or 'right'\n").lower()
if leftOrRight == "left":
  swimOrWait = input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
  if swimOrWait == "wait":
    whichDoor = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if whichDoor == "yellow":
      print("You win!!")
    elif whichDoor == "red":
      print("This door leads to a room of fire, you got burnt. Game over :-(")
    elif whichDoor == "blue":
      print("This door leads to a room of hungry beasties. You got eaten. Game over :-(")
    else:
      print("Game over :-(")
  else:
    print("You have been attacked by a hungry trout. Game over :-(")
else:
  print("You fall into a hole, game over :-(")

'''
We all have played snake, water gun game in our childhood. Write a python program 
capable of playing this game with the user.
1 for Snake
0 for Water
-1 for Gun
'''

import random
# computer=-1
computer=random.choice([1,-1,0])    #uses random module to chose random number
youstr=input("Enter your choice: ")
dict={"Snake":1,"Water":0,"Gun":-1}
reversedict={1:"Snake",0:"Water",-1:"Gun"}

you=dict[youstr]

print(f"You chose {reversedict[you]} \nComputer chose {reversedict[computer]}")

if (you==computer):
    print("Draw")
else:
    if (computer==-1 and you==0):
        print("You  Lose!")
    elif (computer==-1 and you==1):
        print("You  win!")
    elif (computer==1 and you==0):
        print("You  Lose!")
    elif (computer==1 and you==-1):
        print("You  Win!")
    elif (computer==0 and you==1):
        print("You  Win!")
    elif (computer==0 and you==-1):
        print("You  Lose!")
    else:
        print("Something went Wrong")

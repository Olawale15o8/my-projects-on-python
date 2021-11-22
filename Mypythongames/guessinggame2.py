#import random  , math

import   random as rm , math
number = rm.random()
game = math.floor(number * 10 +3)
name= input("your name ")
playerinput = input(f"\n {name.title()}, please guess a number for this game  " )
if (name == playerinput) :
    print(f"{name.title()} , you are right")
else :
    print(f"{name.title()} , you are wrong , {game}  is the correct answer ")


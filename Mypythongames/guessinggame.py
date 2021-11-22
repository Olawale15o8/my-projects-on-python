from random import randint, randrange

nm = input("your name : ")
pl = []
for i in range(3):
    player= int(input("Guess three number that computer may select in random " )) 
    pl.append(player)

rd = []
for i in range(5):
    rd.append(randint(1,10))
incorrect =[]
correct=[]
for i in rd:
    for m in pl:
        if i == m:
            correct.append(i)
            if i != m :
                incorrect.append(i)

anns = set(correct)
anns_2 = set(incorrect)
if len(anns) >= 2 :
    print(f"{nm},  you guess correct numbers withcomputer select {pl} {rd} you win" )
else :
    print(f" you guess some numbers wrong with the computer {pl} {rd} you lose")     
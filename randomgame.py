import random

rock = ">> rock"
paper = ">> paper"
scissors = ">> scissors"

user = int(input("0 = Rock / 1 = Scissors / 2 = Paper >>"))
com = random.randint(0,2)

print("User's pick!")

if user == 0:
    print(rock)
elif user == 1:
    print(scissors)
else:
    print(paper)

print("COM's pick!")

if com == 0:
    print(rock)
elif com == 1:
    print(scissors)
else:
    print(paper)

print("-----RESULT-----")

if user == 0:
    if com == 0:
        print("draw")
    elif com == 1:
        print("User's win")
    else:
        print("COM's win")
elif user == 1:
    if com == 0:
        print("COM's win")
    elif com == 1:
        print("draw")
    else:
        print("User's win")
else:
    if com == 0:
        print("User's win")
    elif com == 1:
        print("COM's win")
    else:
        print("draw")

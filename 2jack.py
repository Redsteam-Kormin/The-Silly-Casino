import os, sys, random, time
from os import system
from time import sleep as s
name = 0
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
clear()
print("-----------------------------")
p1 = input("Player 1 Username: ")
print("-----------------------------")
p2 = input("Player 2 Username: ")
print("-----------------------------")
p1secret = 0
p2secret = 0
p1show = []
p2show = []
actions = ["Stay", "stay", "Hit", "hit", "Fold", "fold"]

p1turn = 0
p2turn = 0

p1win = 0
p2win = 0
p1score = 0
p2score = 0
game = 0
on = 1
startup = 1
clear()
print("")
print("This Game Is Played On 1 Screen With 2 Players, Please Only Let the Player who's turn it is see the screen.")
print("Please Give Screen To Player 1: ", p1)
s(3)
p1stay = 0
p2stay = 0
while on == 1:
    clear()
    if startup == 1:
        p1secret = random.randint(1,10)
        p2secret = random.randint(1,10)
        p1show.append(random.randint(1,10))
        p2show.append(random.randint(1,10))
        startup = 0
        game = 1
    while game == 1:
        if (p1stay == 1 and p2stay == 1) or p1win == 1 or p2win == 1:
            #make win sequence here
            p1score = p1secret
            for x in p1show:
                p1score += x
            p2score = p2secret 
            for x in p2show:
                p2score += x
            if p1score > p2score and p1score <= 21:
                p1win = 1
            elif p2score > p1score and p2score <= 21:
                p2win = 1
            if p1win == 1:
                clear()
                print("")
                print("------+=+=+=O=+=+=+------")
                print(p1, " Wins With ",p1score)
                print("------+=+=+=O=+=+=+------")
                print("")
                on = 0
                game = 0
            elif p2win == 1:
                clear()
                print("")
                print("~<>~<>=-+=-[*]-=+-=<>~<>~")
                print(p2, " Wins With ",p2score)
                print("~<>~<>=-+=-[*]-=+-=<>~<>~")
                print("")
                on = 0
                game = 0
            else:
                clear()
                print("")
                print("]-[]-[]-[]-[]-[]-[]-[]-[]-[")
                print("Both Players Tied With ", p1score)
                print("]-[]-[]-[]-[]-[]-[]-[]-[]-[")
                print("")
                on = 0
                game = 0
        if p1stay == 1 and p2stay != 1:
            p2turn = 1
        if p1turn == 1 and p1stay != 1:
            clear()
            p1score = 0
            p1score += p1secret
            for x in p1show:
                p1score += x
            if p1score > 21:
                p2win = 1
                p1turn = 0
                p1stay = 1
                p2stay = 1
                print(p1, " Went Over 21.")
            while p1turn == 1:
                print(p1)
                print("------------------------------")
                print("Cards: ")
                print("")
                print("Face Down: ", p1secret)
                print("Face Up: ", p1show)
                print("Score: ", p1score)
                print("------------------------------")
                print(p2, "'s Cards: ", p2show)
                print("")
                print("Actions: [Stay] [Hit] [Fold]")
                p1act = str(input("Action: "))
                for x in actions:
                    if p1act == x:
                        if p1act == "Stay" or p1act == "stay":
                            p1stay = 1
                            p1turn = 0
                            p2turn = 1
                            clear()
                            print("Please Switch To Player 2.")
                            s(2)
                            clear()
                        elif p1act == "Hit" or p1act == "hit":
                            p1show.append(random.randint(1,10))
                            p1turn = 0
                            p2turn = 1
                            clear()
                            print("Please Switch To Player 2.")
                            s(2)
                            clear()
                        elif p1act == "Fold" or p1act == "fold":
                            p2win = 1
                            p1turn = 0
        if p2stay == 1 and p1stay != 1:
            p1turn = 1
        if p2turn == 1 and p2stay != 1:
            clear()
            #player 2's score v
            p2score = 0
            p2score += p2secret
            for x in p2show:
                p2score += x    
            if p2score > 21:
                p1win = 1
                p1stay = 1
                p2stay = 1
                p2turn = 0
                print(p2, " Went Over 21.")
            #player 2's score ^
            #player 2's turn v
            while p2turn == 1:
                print(p2)
                print("----------------------------")
                print("Cards: ")
                print("Face Down: ", p2secret)
                print("Face Up: ", p2show)
                print("Score: ", p2score)
                print("----------------------------")
                print(p1, "'s Cards: ", p1show)
                print("")
                print("Actions: [Stay] [Hit] [Fold]")
                p2act = str(input("Action: "))
                for y in actions:
                    if p2act == y:
                        if p2act == "Stay" or p2act == "stay":
                            p2stay = 1
                            p2turn = 0
                            if p1stay == 0:
                                p1turn = 1
                                clear()
                                print("Please Switch To Player 1")
                                s(2)
                                clear()
                            else:
                                clear()
                                print("Please Place Screen Between both Players For Results.")
                                s(3)
                                clear()
                        elif p2act == "Hit" or p2act == "hit":
                            p2show.append(random.randint(1,10))
                            p2turn = 0
                            p1turn = 1
                            clear()
                            print("Please Switch To Player 1")
                            s(2)
                            clear()
                        elif p2act == "Fold" or p2act == "fold":
                            p1win = 1
                            p2turn = 0
        if p1turn == 0 and p2turn == 0:
            p1turn = 1
print("")
print("python3 2jack.py")
print("Type Phrase Above To Replay")
print("")
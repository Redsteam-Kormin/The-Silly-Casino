import os, sys, time, random
from os import system
from time import sleep as s
name = 0
def clear():
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')
#sadly, due to codio's inablility to bring data between runs, this must be updated yourself.
clear()
highuser = "Dylan"
highscore = 837965310
highgame = ["Dice", "Blackjack"]
newhigh = 0
beststreak = 0
showtitle = int(input("Show Big Title? (PC Recommended, 1 for YES, 0 For NO) "))
if showtitle == 1:
    clear()
    print("")
    print(" /$$$$$$$$ /$$                         /$$$$$$                      /$$                    ")
    print("|__  $$__/| $$                        /$$__  $$                    |__/                    ")
    print("   | $$   | $$$$$$$   /$$$$$$        | $$  \__/  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$ ")
    print("   | $$   | $$__  $$ /$$__  $$       | $$       |____  $$ /$$_____/| $$| $$__  $$ /$$__  $$")
    print("   | $$   | $$  \ $$| $$$$$$$$       | $$        /$$$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$")
    print("   | $$   | $$  | $$| $$_____/       | $$    $$ /$$__  $$ \____  $$| $$| $$  | $$| $$  | $$")
    print("   | $$   | $$  | $$|  $$$$$$$       |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$| $$  | $$|  $$$$$$/")
    print("   |__/   |__/  |__/ \_______/        \______/  \_______/|_______/ |__/|__/  |__/ \______/ ")
    print("")                                                                                                              
    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")                                                                                                              
                                                                                                              
else:
    clear()
    print("")
    print("-.- |    _    /¨\      ___ o")
    print(" |  |-. |_|   |   /¨¨\ \_. _ ,_  /¨\\")
    print(" |  | | L_-   \_/ \_/| __/ I | | \_/ ")
    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    print("")
username = str(input("What is Your Name? "))
print("")
money = random.randint(200,2000)
if username == "deadbeatdad":
    money = 100000
    print("Ready To Gamble Your Kid's College Fund?")
luck = 0
ach1 = 0
game = 1
streak = 0
jackwin = 5
dicewin = 5
colorwin = 0
insidewin = 0
losestreak = 0
print("Welcome To The Casino, You have ", money, " dollars. GAMBLE YOUR LIFE AWAY.")
areaselect = 1
while areaselect != 0:
    area = input("Where Do You Want To Play? [Blackjack] [Dice] [Slots] [Roulette] ")
    if area == "Blackjack" or area == "Dice" or area == "Slots" or area == "Roulette":
        areaselect = 0
    else:
        clear()    
        print("Invalid Option, Retry. (Case-Sensitive)")
arealist = []
arealist.append(area)
while money != 0:
    allin = 0
    clear()
    quote = random.randint(0,20)
    print("------Highscore------")
    print("User: ", highuser)
    print("Score: ", highscore)
    print("Game: ", highgame)
    print("---------------------")
    print("")
    print("Name: ", username)
    print("Money: ", money)
    print("Game: ", area)
    print("")
    if quote > 0:
        if quote == 1:
            print("I LOVE GAMBLING")
        elif quote == 2:
            print("Don't Quit Now")
        elif quote == 3:
            print("As RAXDFLIPNOTE once said...")
        elif quote == 4:
            print("It's mathematically impossible to win against the casino, but you can try!")
        elif quote == 5:
            print("Ur doin great lad. :3")
        elif quote == 6:
            print("99% Of Gamblers Quit Before they Win Big!")
        elif quote == 7:
            print("Here at Arby's™, all our food keeps blowing up!")
        elif quote == 8:
            print("Gambling Is Awesome!")
        elif quote == 10:
            print("ohmygod KITTY YAYYYYYYYY")
        elif quote == 11:
            print("'I'm Gonna Touch Gabe, Appropriately.' - Izak Patton")
        elif quote == 12:
            print("Are we so back or are we cooked?")
        elif quote == 13:
            print("The Different Games have different luck and money-making stats!")
        elif quote == 14:
            print("'I need my chinese brainrot app.' - Izak Patton")
        elif quote == 15:
            print("It is Advised To Only Bet half Of what you have... but who cares? GO ALL IN!!!")
        elif quote == 16:
            print("It's Better to Pee In The Shower Than It Is To Shower In The Pee.")
        elif quote == 17:
            print("'All Clothing Is Unisex if you Think About It long enough.' - ghandi, the art of war (i think)")
        elif quote == 18:
            print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")
        elif quote == 19:
            if area == "Blackjack":
                print("The Dealer Lies About Their Score Withing a Range of 1-5 less than what he has. Be sure to account for that when playing!")
            elif area == "Dice":
                print("The Dice Are Luck Based, But They will roll lower the more you've won, and high the more you've lost!")
            elif area == "Slots":
                print("Slots? A True Gambler I See...")
        elif quote == 20:
            print("Part I: Feuerbach. | Opposition of the Materialist and Idealist Outlook | A. Idealism and Materialism | The Illusions of German Ideology")
                

        print("")
    print("Streak: ", streak)
    #rank system:
    if money >= 10000000:
        print("")
        print("Rank: Casino Killer")
    elif money >= 1000000:
        print("")
        print("Rank: Elite Gambler")
    elif money >= 10000:
        print("")
        print("Rank: Average Gambler")
    elif money >= 1000:
        print("")
        print("Rank: Lucky")
    else: 
        print("")
    print("")
    if streak > beststreak:
        beststreak = streak
    if money > highscore:
        highscore = money
        highuser = username
        highgame = arealist
        newhigh = 1
    print("Bet any Number, or type -1, to bet all, or -2 to switch games.")
    action = int(input("How Much Would You Like To Bet? "))
    if action == -1:
        allin = 1
        action = money
    elif action == -2:
        areaselect = 1
        clear()
        while areaselect != 0:
            print("[Blackjack] [Dice] [Slots] [Roulette]")
            area = input("What Do You Want To Play? ")
            if area == "Blackjack" or area == "Dice" or area == "Slots" or area == "Roulette":
                areaselect = 0
                action = money+1
                if not area in arealist:
                    arealist.append(area)
            else:
                print("Invalid Option, Retry. (Case-Sensitive)")
    if action <= money or not action >= 0:
        if area == "Blackjack":
            clear()
            jackwin = 0
            jackplay = 1
            playertotal = 0
            dealertotal = 0
            dealer = []
            player = []
            dealer.append(random.randint(1,10))
            dealer.append(random.randint(1,10))
            player.append(random.randint(1,10))
            player.append(random.randint(1,10))
            while jackplay == 1:
                dealertotal = 0
                playertotal = 0
                for x in dealer:
                    dealertotal += x
                for y in player:
                    playertotal += y
                if dealertotal > 7:
                    print("Dealer: ", dealertotal - random.randint(1,5))
                else:
                    print("Dealer: ", random.randint(2,10))
                    hint = random.randint(1,10)
                    if hint < 8 and hint > 5:
                        print("Random Guy: Hey dude! The Dealer's Lying! His Score is Between 1 and 7!")
                print(username,":", player)
                print("")
                print("Actions: [Stay] [Hit] [Fold] [Guess] [Score]")
                print("")
                actionjack = input("Your Action? ")
                if actionjack == "Stay" or actionjack == "Hit" or actionjack == "Fold" or actionjack == "Guess" or actionjack == "Score":
                    if actionjack == "Stay":
                        if dealertotal < playertotal and dealertotal < 18:
                            dealer.append(random.randint(1,10))
                            dealertotal = 0
                            for x in dealer:
                                dealertotal += x
                            print("Dealer Hit")
                        else:
                            print("Dealer Stays...")
                            s(.5)
                        if dealertotal > 21:
                            dealerlose = dealertotal
                            dealertotal = 0
                            print("Dealer Lost...")
                            print("Dealer Had ", dealerlose)
                            s(2)
                        if playertotal > dealertotal:
                            jackwin = 1
                            jackplay = 0
                            clear()
                        elif playertotal == dealertotal:
                            jackwin = 2
                            jackplay = 0
                            clear()
                        elif dealertotal > playertotal:
                            jackwin = 0
                            jackplay = 0
                            clear()
                    elif actionjack == "Hit":
                        player.append(random.randint(1,10))
                        playertotal = 0
                        for y in player:
                            playertotal += y
                            if playertotal > 21:
                                jackwin = 0
                                jackplay = 0
                                clear()
                        clear()
                    elif actionjack == "Fold":
                        if playertotal < dealertotal:
                            jackwin = 2
                            jackplay = 0
                            clear()
                        elif playertotal > dealertotal:
                            jackwin = 0
                            jackplay = 0
                            clear()
                    elif actionjack == "Guess":
                        guess = int(input("What Is The Dealer's Score? (Hint: The Chart Is Untrue): "))
                        if guess == dealertotal:
                            jackwin = 1
                            jackplay = 0
                            clear()
                            print("You Guessed Correctly!")
                            s(1)
                            clear()
                        else:
                            clear()
                            print("EHHHHH, WRONG")
                            s(2)
                            jackwin = 0
                            jackplay = 0
                            clear()
                    elif actionjack == "Score":
                        print("Your Current Score Is")
                        print("")
                        print(playertotal)
                        print("")
                else:
                    print("Invalid Option, Retry. (Case-Sensitive)")
        elif area == "Roulette":
            insidewin = 0
            colorwin = 0
            spinchoice = 0
            while spinchoice != 1:
                clear()
                print("Color: Bet on Red or Black for a small prize.")
                print("Number: Bet On Any Number Between 1 and 50 for a massive prize!")
                print("")
                betchoice = input("What would You like To bet on? [Color] [Number]")
                if betchoice == "Color":
                    colorpick = 0
                    clear()
                    while colorpick != 1:    
                        colorchoice = input("Red or Black? (50/50) ")
                        if colorchoice == "Red":
                            colorpick = 1
                        elif colorchoice == "Black":
                            colorpick = 1 
                        else:
                            print("Invalid color Choice.")
                    colortonumber = 0
                    if colorchoice == "Red":
                        colortonumber = 1
                    elif colorchoice == "Black":
                        colortonumber = 2
                    spinchoice = 1
                elif betchoice == "Number":
                    numberpick = 0
                    clear()
                    while numberpick != 1:
                        numberchoice = int(input("Select A Number 1 to 50: "))
                        if numberchoice > 0 and numberchoice < 51:
                            numberpick = 1
                            spinchoice = 0

                        else:
                            print("Invalid Number Choice, Retry. (1-50)")
                else:
                    print("Invalid Choice, Retry. (Case-Sensitive)")
            wincolor = random.randint(1,2)
            winnumber = random.randint(1,50)
            if betchoice == "Color":
                if colortonumber == wincolor:
                    colorwin = 1
                    clear()
            elif betchoice == "Number":
                if numberchoice == winnumber:
                    insidewin = 1
                    clear()
            else:
                clear()
                



        elif area == "Dice":
            clear()
            playerdice = []
            house = []
            house.append(random.randint(1,6))
            house.append(random.randint(1,6))
            if losestreak <= 3 and streak <= 3:
                playerdice.append(random.randint(1+losestreak,6))
                playerdice.append(random.randint(1+streak,6))
            elif losestreak > 3:
                playerdice.append(random.randint(4,6))
                playerdice.append(random.randint(3,6))
            elif streak > 3:
                playerdice.append(random.randint(1,6))
                playerdice.append(random.randint(1,4))
            diceplay = 1
            housetrade = 0
            dicetrade = 0
            urcooked = 0
            while diceplay != 0:
                housetotal = 0
                dicetotal = 0
                for x in house:
                    housetotal += x
                for y in playerdice:
                    dicetotal += y
            
                print("---------=====---------")
                print("House: ", house)
                print("")
                print(username,": ", playerdice)
                print("---------=====---------")
                if housetotal > dicetotal and dicetrade == 1:
                    print("")
                    print("I Hope You didn't go All In!")
                    print("")
                print("Actions: [Stay] [Trade]")
                diceact = input("Action: ")
                if diceact == "Stay" or diceact == "Trade":
                    if diceact == "Stay":
                        clear()
                        if housetotal >= dicetotal:
                            for x in house:
                                if x > 6 and housetrade != 1:
                                    house.remove(x)
                                    house.append(random.randint(1,6))
                                    housetrade = 1
                            housetotal = 0
                            for x in house:
                                housetotal += x
                        if dicetotal > housetotal:
                            dicewin = 1
                            diceplay = 0
                        elif dicetotal == housetotal:
                            dicewin = 2
                            diceplay = 0
                        else: 
                            dicewin = 0
                            diceplay = 0
                    elif diceact == "Trade" and dicetrade != 1:
                        clear()
                        print("Your Dice: ", playerdice)
                        print("Total: ", dicetotal)
                        print("")
                        tradeact = int(input("What Dice Would You Like To Trade? (1-6 Integer Value) "))
                        for f in playerdice:
                            if f == tradeact and dicetrade != 1:
                                playerdice.remove(f)
                                playerdice.append(random.randint(1,6))
                                dicetrade = 1
                    elif diceact == "Trade" and dicetrade == 1:
                        clear()
                        print("Trade Already Made, Invalid.")
                else:
                    clear()
                    print("Invalid Action, Retry. (Case-Sensitive)")
        elif area == "Slots":
            luck = random.randint(1+losestreak,20-streak)
        if luck > 10 or jackwin == 1 or dicewin == 1:
            calc = 0
            calc = action*2
            if area == "Roulette":
                money = money + (action*(2+losestreak+streak))
            else:
                money = money + (action*2)
            if area == "Slots":
                clear()
                print("[O][O][O]")
                s(.3)
                clear()
                print("[O][X][O]")
                s(.3)
                clear()
                print("[O][X][X]")
                s(.3)
                clear()
                print("[X][X][X]")
            elif area == "Blackjack":
                print("Dealer had ", dealertotal)
                print("")
            print("You Made ", calc, "Dollars!")
            s(1)
            streak += 1
            losestreak = 0
        elif jackwin == 2:
            print("You Tied With The Dealer. No Money Was Gained or Lost.")
            s(2)
            streak = 0
            losestreak = 0
        elif dicewin == 2:
            print("You tied with the House, No Money was Gained or Lost.")
            s(2)
            streak = 0
            losestreak = 0
        elif colorwin == 1:
            money = money*(2+losestreak)
        elif insidewin == 1:
            money = money*(10+(losestreak*losestreak))
        else:
            if area == "Slots":
                clear()
                print("[X][O][O]")
                s(.3)
                clear()
                print("[O][X][X]")
                s(.3)
                clear()
                print("[X][O][X]")
                s(.3)
                clear()
                print("[O][O][X]")
            calc = 0
            calc = action
            money -= action    
            print("You lost ", calc, "Dollars.")
            streak = 0
            losestreak +=1
            s(1)
clear()
object = random.randint(1,10)
if object == 1:
    object = "Cheeseburger"
elif object == 2:
    object = "2007 Nissan Altima"
elif object == 3:
    object = "Whole Walmart™ Bread Section You Always Wanted"
elif object == 4:
    object = "3 Whole Popcorn Kernels"
elif object == 5:
    object = "Highscore"
elif object == 6:
    object = "Sexual Relations with ",highuser
elif object == 7:
    object = "5 Trillion Dollars"
elif object == 8:
    object = "Private Airliner"
elif object == 9:
    object = "death by gettin' shot in the head, just like JFK"
elif object == 10:
    object = "One Gallon of Whole Milk. All to yourself"
print("You Lost.")
print("Betting ", action, " made you lose.")
if area == "Blackjack":
    jacklosscalc = dealertotal - playertotal
    print("Dealer Had ", dealertotal, ", ", jacklosscalc, "more than you.")
print("Highest Streak: ", beststreak)
print("")
print("Never Give Up On That",object,"!")
print("")
if newhigh == 1:
    print("New Highscore!")
    print("-------------------")
    print(username)
    print(highscore)
    print(area)
    print("-------------------")
    print("Go Tell Dylan Nemeth So It Can Be Updated.")
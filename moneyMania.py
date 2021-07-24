import os
import random
import pickle
import os.path
import json
from asyncio import sleep

#all variables
playerName = ""
moneyInhand = 100
moneyInbank = 0
netWorth = moneyInbank + moneyInhand
command = ""
inventory = []
CommonPrice = 45    #for fish
UncommonPrice = 65   #for fish
LegendaryPrice = 115   #for fish
fishRodUses = 10
food = []
workAmt = 10
reputation = 100

#function for getting valid option
def getvalidOpt(mini, maxi, intVal):
        try:
            intVal = int(intVal)
            if intVal is not None and intVal >= mini and intVal <= maxi:
              return intVal
            else:
              intVal = getvalidOpt(mini, maxi, input("Please enter a valid number: "))
              return intVal  
        except ValueError:
            intVal = None
            intVal = getvalidOpt(mini, maxi, input("Please enter a valid number: "))
            return intVal

def validateVal(v):
    try:
        x = float(v)
        return x
    except:
        x=validateVal(input("Please enter a valid number: "))
        return x

def help():
    print('''There are various commands in this game to achieve tasks. Here is a list of all commands and their functions:
[1] st : to view your stats
[2] dep : to deposit money in ManiaBank
[3] wd : to withdraw money from ManiaBank
[3] wk : to work
[4] s : to do some shopping from ManiaMart
[5] in : to view your inventory
[6] sl : sell things from your inventory
[7] f : to go fishin'! (if you have a fishing rod)
[8] slots : to try your luck in slots!
[9] e : to eat food (if you have any)
[10] lb : leaderboard
[11] rob : to rob, if you feel evil...
[12] ch : charity
[13] hcmd : to get more information on any particular command.
\r''')

def helpCmd():
    helpsdict = {"st":"This command will help you check your money and reputation.", "dep":"This command will help you deposit money in the bank. Depositing is very important, as your money will stay safe from robbers.", "wd":"This command is to withdraw money from the bank, in case you need it.", "wk":"This command is to work and earn (or lose) money. As you earn less by working, the losses are low too, so it is a good way to start off your money-earning journey. But remember, you can only work for 10 days continuously, then you will get exhausted. To replenish you energy, you'll have to buy some food or energy drinks from ManiMart and consume it.", "s":"This command is to shop in ManiaMart, you'll notice most of the products in ManiaMart will be instrumental in helping you earn money, so yeah, don't hesitate to spend some money too...", "in":"This command is to view your inventory, or all the things that you own. You can also seel some stuff from your inventory to earn some good cash!", "sl":"By this command, you can sell stuff from your inventory, if you have any.", "f":"To go fishing, this command works only if you have a fishing rod. You can always buy one from ManiaMart. Also, you can sell the fish you caught! But the fishing rods ManiaMart sells are quite defective and break after a few uses ,so you'll have to buy another fishing rod from the shop.", "slots":"This command is to go to ManiaCasino and try the slots machine. But to do so, you'll have to buy a slots tokan from ManiaMart.", "e":"To eat the food, if you've bought it from ManiaMart.", "lb":"To see the leaderboard of the richest people in ManiaTown. To win the game, you have to become the richest person in ManiaTown.", "rob":"To steal some money, of course, you can get a lot of money, but the losses too are equally high. Also, your reputation in ManiaTown decreases if you get caught. And you lose the game if your reputation becomes zero!", "ch":"To give some money in charity. If your reputation has decreased, you can give money in charity to redeem your honour. If your reputation is 100, it will not increase any further.", "0":False}

    cont = True
    
    while cont == True:    
        help = str.lower(input("What command do you need help with?(Press '0' to exit): "))
        
        if help in helpsdict:
            if help in helpsdict and help != "0":
                print(helpsdict[help])
                print("\r")
            elif help == '0':
                cont = helpsdict["0"]
                print("Thank You!")
                print("\r")
        
        else:
            print("Command not found! Please try again.")
            print("\r")

def stats():
    print('''In hand : {} Mbs
In ManiaBank : {} Mbs
Net Worth : {} Mbs
Reputation : {}  
\r''' . format(moneyInhand,moneyInbank,netWorth,reputation))

def deposit():
    global moneyInhand
    global moneyInbank
    global netWorth
    
    amtDep = getvalidOpt(0, moneyInhand, input("How much money do you want to deposit?: "))
    moneyInhand -= amtDep
    moneyInbank += amtDep
    netWorth = moneyInbank + moneyInhand
    print("{} Mbs successfully deposited in ManiaBank." . format(amtDep))
    print("\r")

async def get_money():
    global moneyInhand
    global moneyInbank
    global netWorth

    while True:
        await sleep(5)
        
        amtGet = random.randint(50,100)

        moneyInhand += amtGet
        netWorth = moneyInbank + moneyInhand

def withdraw():
    global moneyInhand
    global moneyInbank
    global netWorth
    
    amtWdr =  getvalidOpt(0, moneyInbank, input("How much money do you want to withdraw?: "))
    moneyInhand += amtWdr
    moneyInbank -= amtWdr
    netWorth = moneyInbank + moneyInhand
    print("{} Mbs successfully withdrawn from ManiaBank." . format(amtWdr))
    print("\r")

def eat():
    global workAmt
    global inventory
    
    if len(food) > 0:
        print("Here is all the food you have: ")
        
        for i in range(len(food)):
            print("[{}]" . format(i+1),food[i])
        print("\r")
        
        foodChoice = getvalidOpt(0, len(food), input("What do you want to eat? (type the serial number of the food item, press 0 to exit): "))
        
        foodEaten = food[foodChoice-1]
        
        if foodEaten == "Energy Drink":
            workAmt = 15
            print("You have energized yourself enough to do work for 15 days continuously!")
            food.remove('Energy Drink')
            inventory.remove('Energy Drink')
            print("\r")
        
        elif foodEaten == "Mega Meal":
            workAmt = 35
            print("You have energized yourself enough to do work for 35 days continuously!")
            food.remove('Mega Meal')
            inventory.remove('Mega Meal')
            print("\r")

        elif foodChoice == 0:
            print("You exit successfully.")
            print("\r")
    else:
        print("You have no food as of now!")
        print("\r")

def work():
    global moneyInhand
    global moneyInbank
    global netWorth
    global workAmt
    
    workProfit = random.randint(40,50)
    workLoss = random.randint(10,20)
  
    workScenarios = ["You worked and earned {} Mbs!" . format(workProfit), "You worked, but messed up! You were fined {} Mbs." . format(workLoss)]
    workScenario = random.choice(workScenarios)
    
    if workAmt > 0:
        print(workScenario)
        workAmt -= 1
       
        print("\r")
        
        if workScenario == workScenarios[0]:
            moneyInhand += workProfit
            netWorth = moneyInbank + moneyInhand
        
        elif workScenario == workScenarios[1]:
            moneyInhand -= workLoss
            netWorth = moneyInbank + moneyInhand

    else:
        print("You have worked a lot and have exhausted! To energize yourself, buy an energy drink from ManiaMart. If you want to work more, buy a mega meal.")
        print("\r")

def shop():
    global moneyInhand
    global netWorth
    global fishRodUses
    
    item = getvalidOpt(0, 4, input('''Welcome to ManiaMart! What would you like to buy?: 
[1] Fishing rod - 40 Mbs
[2] Slots Token - 100 Mbs
[3] Energy Drink - 50 Mbs
[4] Mega Meal - 100 Mbs
Type in the serial number of your choice (Press 0 to exit): '''))
    print("\r")
    
    if item == 1:
        if moneyInhand >= 40:
            inventory.append('Fishing Rod')
            fishRodUses = 10
            moneyInhand -= 40
            netWorth = moneyInbank + moneyInhand
            print("Successfully bought fishing rod.")
            print("\r")
        else:
            print("You do not have enough money in hand to buy this product!")
    
    elif item == 2:
        if moneyInhand >= 100:
            inventory.append('Slots Token')
            moneyInhand -= 100
            netWorth = moneyInbank + moneyInhand
            print("Successfully bought Slots Token.")
            print("\r")
        else:
            print("You do not have enough money in hand to buy this product!")

    elif item == 3:
        if moneyInhand >= 50:
            inventory.append('Energy Drink')
            food.append('Energy Drink')
            moneyInhand -= 50
            netWorth = moneyInbank + moneyInhand
            print("Successfully bought energy drink.")
            print("\r")
        else:
            print("You do not have enough money in hand to buy this product!")

    elif item == 4:
        if moneyInhand >= 120:
            inventory.append('Mega Meal')
            food.append('Mega Meal')
            moneyInhand -= 100
            netWorth = moneyInbank + moneyInhand
            print("Successfully bought mega meal.")
            print("\r")
        else:
            print("You do not have enough money in hand to buy this product!")
    
    elif item == 0:
        print("See you later!")

def inventoryView():
    if len(inventory) > 0:
        print("Here's your inventory: ")
        for i in range(len(inventory)):
            print("[{}]" . format(i+1),inventory[i])
        print("\r")
    else:
        print("You have nothing in your inventory!")
        print("\r")

def fishing():
    global fishRodUses
    global inventory
    
    fishes = ["Common Fish","Common Puffer Fish","Common Clown Fish","Common Lobster","Common Squid","Uncommon Swordfish","Uncommon Baby Shark","Uncommon Salmon","Uncommon Duck","Legendary Shark"]
    fishCaught = random.choice(fishes)
    
    fishingScenarios = ["You just caught a {}!" . format(fishCaught),"You just caught a {}, but it slapped you and swam back in the water..." . format(fishCaught)]
    fishingScenario = random.choice(fishingScenarios)
    
    CommonPrice = 45
    UncommonPrice = 65
    LegendaryPrice = 115
    
    if "Fishing Rod" in inventory:
        if fishRodUses <= 0:
            print("Oops! You Fishing Rod snapped. You'll have to buy another one from ManiaMart...")
            inventory.remove('Fishing Rod')
            print("\r") 
        else:
            print(fishingScenario)
            print("\r")
            if fishingScenario == fishingScenarios[0]:
                if "Common" in fishCaught:    
                    print("You can get {} Mbs for this fish." . format(CommonPrice))
                    print("\r")
                    inventory.append(fishCaught)
                    fishRodUses -= 1
                   
                elif "Uncommon" in fishCaught:
                    print("You can get {} Mbs for this fish." . format(UncommonPrice))
                    print("\r")
                    inventory.append(fishCaught) 
                    fishRodUses -= 1
                    
                elif "Legendary" in fishCaught:
                    print("You can get {} Mbs for this fish." . format(LegendaryPrice))
                    print("\r")
                    inventory.append(fishCaught)    
                    fishRodUses -= 1
                    
            elif fishingScenario == fishingScenarios[1]:
                fishRodUses -= 1
                 
    else:
        print("You dont have a Fishing Rod! You'll have to buy one from ManiaMart.")  
        print("\r")

def sell():
    global netWorth
    global moneyInhand

    if len(inventory) > 0:
        print("Here's your inventory: ")
        for i in range(len(inventory)):
            print("[{}]" . format(i+1),inventory[i])
        #sell = getvalidOpt(1, len(inventory)+1, input("What do you want to sell?(Type in the serial number of your choice): "))
        #choice = inventory[sell-1]
        print("\r")
        print("You'll have to enter the start and end serial number, then all items in that range will be sold.")
        sellStart = getvalidOpt(1, len(inventory), input("Type in the start serial number: "))
        sellEnd = getvalidOpt(1, len(inventory), input("Type in the end serial number: "))
        print("\r")
        for i in inventory[sellStart-1:sellEnd+1]:
            if i == "Fishing Rod":
                print("Sorry! You can't sell a fishing rod.")
            
            elif i == "Slots Token":
                print("Sorry! You can't sell a slots token.")

            elif i == "Energy Drink":
                print("Sorry! You can't sell an energy drink.")
            
            elif i == "Mega Meal":
                print("Sorry! You can't sell a mega meal.")
            
            elif "Uncommon" in i:
                print("Successfully sold {}" . format(i))
                inventory.remove(i)
                moneyInhand += UncommonPrice
                netWorth = moneyInbank + moneyInhand
        
            elif "Common" in i:
                print("Successfully sold {}" . format(i))
                inventory.remove(i)
                moneyInhand += CommonPrice
                netWorth = moneyInbank + moneyInhand

            elif "Legendary" in i:
                print("Successfully sold {}" . format(i))
                inventory.remove(i)
                moneyInhand += LegendaryPrice
                netWorth = moneyInbank + moneyInhand
        print("\r")
    else:
        print("There is nothing to sell in your inventory!")
        print("\r")

def slots():
    global moneyInhand
    global moneyInhand
    global netWorth

    if "Slots Token" in inventory:
        print("Welcome to ManiaLottery!")
        inventory.remove('Slots Token')
        
        if str(input("Press 'y' to spin the slots: ")) == 'y':
            ran1 = random.randint(0,3)
            ran2 = random.randint(0,3)
            ran3 = random.randint(0,3)            
            print("\r")
            print('''
    |   |   |   |
--> | {} | {} | {} |
    |   |   |   |
    '''. format(ran1,ran2,ran3))
            if ran1 == ran2 == ran3:
                print("\r")
                print('''Yay! You won a JACKPOT of 1000 Mbs!!!!''')
                moneyInhand += 1000
                netWorth = moneyInhand + moneyInbank
            else:
                print("\r")
                print("Oh, you did not win anything. Better luck next time!")
    
    else:
        print("You dont have a Slots Token! Go buy one from ManiaMart.")
        print("\r")

def leaderboard():
    lb = [[10000,"The Queen"],[9000,"Mr Beast"],[8000,"The Mayor"],[7000,"The Owner of ManiaMart"],[5000,"Some random rich kid"],[netWorth,"You"],[1000,"An average person"],[100,"A poor person"]]

    lb.sort(reverse = True)
    
    print("Here is the leaderboard:")
    for i in range(len(lb)):
        print("[{}]" . format(i+1),lb[i][1],"-",lb[i][0])

def rob():
    global moneyInhand
    global moneyInbank
    global netWorth
    global reputation
    
    reputation = 100
    robProfit = random.randint(400,500)
    robLoss = random.randint(100,200)
  
    robScenarios = ["You robbed and got {} Mbs!" . format(robProfit), "You robbed, but were caught! You were fined {} Mbs. And you reputation decreased by 20" . format(robLoss)]
    robScenario = random.choice(robScenarios)

    print(robScenario)

    if robScenario == robScenarios[0]:
        moneyInhand += robProfit
        netWorth = moneyInbank + moneyInhand
        
    elif robScenario == robScenarios[1]:
        moneyInhand -= robLoss
        netWorth = moneyInbank + moneyInhand
        reputation -= 20

def charity():
    global moneyInhand
    global moneyInbank
    global netWorth
    global reputation

    print("Welcome to 'ManiaTown Cares'! For increasing reputation by 20, donate more than 500 Mbs, if you want to increase your reputation by 50, donate 1000 Mbs. If your reputation is 100, it will not increase, as it is maximum.")
    charity = validateVal(input("Enter how much money do you want to give in charity: "))

    if charity >= 100:    
        if charity >= 1000:
            moneyInhand -= 1000
            netWorth = moneyInhand + moneyInbank
            reputation += 50
            if reputation > 100:
                reputation = 100
            print("{} Mbs given in charity. Your reputation has incresed by 40" . format(charity))
        
        elif charity >= 500:
            moneyInhand -= 500
            netWorth = moneyInhand + moneyInbank
            reputation += 20
            if reputation > 100:
                reputation = 100
            print("{} Mbs given in charity. Your reputation has incresed by 20" . format(charity))

    else:
        if charity >= 1000:
            moneyInhand -= 1000
            netWorth = moneyInhand + moneyInbank
            print("You gave {} Mbs in charity. But your reputation will not increase as your reputation is already maximum.")
            
        elif charity >= 500:
            moneyInhand -= 500
            netWorth = moneyInhand + moneyInbank
            reputation += 20
            print("You gave {} Mbs in charity. But your reputation will not increase as your reputation is already maximum.")

#This finds commands and calls the respective functions.
cmds = {"st":stats,"dep":deposit,"wd":withdraw,"wk":work,"h":help,"s":shop,"f":fishing,"in":inventoryView,"sl":sell,"slots":slots,"e":eat,"lb":leaderboard,"rob":rob,"ch":charity,"hcmd":helpCmd}

global data

data = {'playerName':playerName, 'moneyInhand_n':moneyInhand, 'moneyInbank_n':moneyInbank, 'netWorth_n':netWorth, 'inventory_n':inventory, 'CommonPrice_n':CommonPrice, 'UncommonPrice_n':UncommonPrice, 'LegendaryPrice_n':LegendaryPrice, 'fishRodUses_n':fishRodUses, 'food_n':food, 'workAmt_n':workAmt, 'reputation_n':reputation} 

newPlayer = True

if os.path.exists('gameData.dat') == True:
    with open('gameData.dat','rb') as f:
        data = pickle.load(f)

    newPlayer = False

    playerName = data['playerName']
    moneyInhand = data['moneyInhand_n']
    moneyInbank = data['moneyInbank_n']
    netWorth = data['netWorth_n']
    inventory = data['inventory_n']
    CommonPrice = data['CommonPrice_n']
    UncommonPrice = data['UncommonPrice_n']  
    LegendaryPrice = data['LegendaryPrice_n']
    fishRodUses = data['fishRodUses_n']
    food = data['food_n']
    workAmt = data['workAmt_n']
    reputation = data['reputation_n']

    doReset = str.lower(input("Welcome back {}! press 'y' to continue your existing game: " . format(playerName)))  

    if doReset != 'y':
        #all variables
        playerName = ""
        moneyInhand = 100
        moneyInbank = 0
        netWorth = moneyInbank + moneyInhand
        command = ""
        inventory = []
        CommonPrice = 45    #for fish
        UncommonPrice = 65   #for fish
        LegendaryPrice = 115   #for fish
        fishRodUses = 10
        food = []
        workAmt = 10
        reputation = 100 
        data = {'playerName':playerName, 'moneyInhand_n':moneyInhand, 'moneyInbank_n':moneyInbank, 'netWorth_n':netWorth, 'inventory_n':inventory, 'CommonPrice_n':CommonPrice, 'UncommonPrice_n':UncommonPrice, 'LegendaryPrice_n':LegendaryPrice, 'fishRodUses_n':fishRodUses, 'food_n':food, 'workAmt_n':workAmt, 'reputation_n':reputation}

        playerName = str(input("Enter a new username: "))  
else:
    playerName = str(input("Enter a username: "))  

#introduction
print("Hello {}! Welcome to Money Mania. You have come to the city from your village, in hopes to earn more money. You have {} Mbs ({} Mania Bucks) in hand. You dream is to be the richest person in ManiaTown. Remember, though, ManiaTown is known for its thieves... So keep depositing your money in ManiaBank so it stays safe. Earn your way to strike it rich. Good luck!" . format(playerName,moneyInhand,moneyInhand))
print("\r")

while True:   

    if 0 < netWorth < 10000:    
        command = str.lower(input("Enter command(If you need help, type \"h\"): "))
        os.system("cls || clear")
        if command in cmds.keys():
                cmds[command]()    
                if moneyInhand > 1000 and netWorth > 3000:
                    print("Oh no! You forgot to deposit your money, and someone robbed 800 Mbs from your house!")
                    netWorth = moneyInhand + moneyInbank
                    moneyInhand -= 800
        else:
            print("Command not found. Please try again")

        data = {'playerName':playerName, 'moneyInhand_n':moneyInhand, 'moneyInbank_n':moneyInbank, 'netWorth_n':netWorth, 'inventory_n':inventory, 'CommonPrice_n':CommonPrice, 'UncommonPrice_n':UncommonPrice, 'LegendaryPrice_n':LegendaryPrice, 'fishRodUses_n':fishRodUses, 'food_n':food, 'workAmt_n':workAmt, 'reputation_n':reputation} 

        with open('gameData.dat', 'wb') as f:
            pickle.dump(data, f)

    elif netWorth <= 0:
        print("Oh no! You had come to ManiaTown to become rich, but you've become bankrupt! You go back to the village and start farming...")
        print("\r")
        break

    elif netWorth > 10000:
        print('''Congrats! You have fulfilled your wish of being the richest man in the world!
                  
                  
                  $$$
                  $$$                        
               $$$$$$$$
             $$$$$$$$$$$$
            $$$   $$$  $$$ 
           $$$    $$$   $$$
           $$$    $$$
           $$$    $$$
            $$$   $$$ 
             $$$$$$$$$$$$            
                  $$$  $$$
                  $$$    $$$
                  $$$     $$$  
                  $$$     $$$
           $$$    $$$    $$$
            $$$   $$$  $$$  
              $$$$$$$$$$
               $$$$$$$   
                  $$$
                  $$$ 
                  
                  ''')  
        break  

    elif reputation <= 0:
        print("Oh no! Your reputation in ManiaTown has SHATTERED! You go back to your village, but get caught and are put in prison...")
        break
                

import time
import random
#=====================================================================
def gamestart():
    slot=['🎰', '🎰', '🎰']
    emojis=['🌮','🥤','🍔','🍕','🍖','🥪','🍙']
    
    def game(z):
        while True:
            times = int(input(f"Spin Slot{z+1} (number of times)\n>"))
            if times>10:
              print("Max! Please try again from the start!")
              continue
            break
            
        while times>1:
            a = random.choice(emojis)
            print(a)
            times-=1
            time.sleep(0.5)
        
        print("\nFinal:")
        time.sleep(0.5)
        a = random.choice(emojis)
        slot[z] = a
        print(slot)
        print()
#=====================================================================
    def check():
        seen = []
        duplicates = []
        for a in slot:
            if a in seen:
                duplicates.append(a)
            else:
                seen.append(a)
                
        global money, betmoney
        
        if len(duplicates)==2:
            print("You won the Jackpot!")
            print(f"You won ${betmoney*2}")
            money += betmoney*2
            print(f"Your total now is ${money}")
        elif len(duplicates)==1:
            print("You won!")
            print(f"You won ${betmoney}")
            money += betmoney
            print(f"Your total now is ${money}")
        else:
            print("You lost...")
            print(f"You lost ${betmoney}")
            money -= betmoney
            print(f"Your total now is ${money}")
        if money > 0: 
            yn1 = str(input("Play again?(y/n)\n>")).lower()
            if yn1=="y":
                return "play"
            else:
                return "quit"
        else:
            print("No more money. Bye.")
            return "quit"
#=====================================================================
    game(0)
    game(1)
    game(2)
    return check()

def bettingphase():
    global betmoney, money
    print(f"{user}:You have ${money}")
    while True:
        try:
            betmoney = int(input("How much money you want to bet?\n>$"))
            if 0<betmoney<=250:
                print("C'mon, dont be a coward! Whatever man!")
            elif 250<betmoney<=500:
                print("Wow, a little bold, Senorita! Could be better man!")
            elif 500<betmoney<=750:
                print("Going crazy - I like it! But not enough man!")
            elif 750<betmoney<=1000:
                print("Holy brochacho, woah, dont be too cocky, Amigo!")
            elif betmoney>money or betmoney<=0:
                print("Invalid bet amount! Try again!")
                continue
            break
            
        except ValueError:
            print("Please enter a valid number")
#=====================================================================
def start():
    while True:
        bettingphase()
        yn = str(input(f"Confirm:${str(betmoney)}?(y/n)\n>")).lower()
        if yn =="y":
            result=gamestart()
            if result=="quit":
                break
            elif result=="play":
                continue
        elif yn =="n":continue
        else:print("Invalid input, try again")
#=====================================================================
print("Welcome to Slot")
time.sleep(0.2)
user = "Timmy"
print("The rules of this game are simple: Spin the wheel a number of times to get a emoji; get the 3 same numbers in a row and you win!")
time.sleep(0.5)
money = 1000
betmoney = 0

start()


#Add a leaderboard to track high scores
#Add difficulty levels (more/fewer emojis)
#Add a statistics display (wins/losses ratio)
#Add sound effects when winning
#Add colors to the output using the colorama library    

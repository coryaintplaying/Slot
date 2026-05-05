import time
import random
#=====================================================================
def gamestart():
    slot=['🎰', '🎰', '🎰']
    emojis=['🌮','🥤','🍔','🍕','🍖','🥪','🍙']
    
    def game(z):
        times = int(input(f"Spin Slot{z+1} (number of times)\n>"))
        if times>10:
          print("Max! Please try again from the start!")
          game(z)
        else:
            while times>1:
                a = random.choice(emojis)
                print(a)
                times-=1
                time.sleep(0.5)
        
            print("\nFinal:")
            time.sleep(1)
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
            print("You won ${betmoney*2}")
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
            yn1 = str(input("Play again?(y/n)\n>"))
            if yn1=="y":
                start()
            if yn1=="n":
                print("Bye, game ends here.")
                break
        else:
            print("No more money. Bye.")
            break
#=====================================================================
    game(0)
    game(1)
    game(2)
    check()

def bettingphase():
    global betmoney, money
    print(f"{user}:You have ${money}")
    try:
        betmoney = int(input("How much money you want to bet?\n>$"))
        if betmoney>money or betmoney<=0:
            print("Invalid bet amount! Try again!")
            bettingphase()
    except ValueError:
        print("Please enter a valid number")
        bettingphase()
#=====================================================================
def start():
    while True:
        bettingphase()
        yn = str(input(f"Confirm:${str(betmoney)}?(y/n)\n>"))
        if yn.lower() =="y":
            print("Game starting, redirecting...")
            result=gamestart()
            if result=="quit":break
        elif yn.lower()=="n":continue
        else:print("Invalid input, try again")
#=====================================================================
print("Welcome to Slot")
time.sleep(1)
user = str(input("Username:"))
print("The rules of this game are simple: Spin the wheel a number of times to get a number; get the 3 same numbers in a row and you win!")
time.sleep(1)
money = 1000
betmoney = 0

start()

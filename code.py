import time
import random

def gamestart():
    global a
    a = 0
    global b
    b = 0
    global c
    c = 0
    jackpot="99"

    slot=[0,0,0]
        
    def game(z):
        print(input("Spin (enter any key)\n>"))
        times = random.randint(1,10)
        while times>1:
            a = random.randint(1,10)
            slot.pop(z)
            slot.insert(z,a)
            print(slot)
            times-=1
            time.sleep(0.5)
        if times==1:
          print("\nFinal:");time.sleep(1)
          a = random.randint(1,10)
          slot.pop(z)
          slot.insert(z,a)
          print(slot)
          times-=1
          print("\n")
        """
        print(input("Spin (enter any key)?\n>"))
        times = random.randint(1,10)
        while times>0:
            b = random.randint(1,10)
            slot.pop(1)
            slot.insert(1,b)
            print(slot)
            times-=1
        times = int(input("How much times do you want to spin the lever for slot 2?\n>"))
        if times<=10:
            while times>0:
                c = random.randint(1,10)
                slot.pop(2)
                slot.insert(2,c)
                print(slot)
                times-=1
        """
    def check():
        seen = []
        duplicates = []
        duplicates1 = []
        for a in slot:
            if a in seen:
                duplicates.append(a)
            elif a in duplicates:
                duplicates1.append(a)
            else:
                seen.append(a)
        if len(duplicates1)==1:
            print("You won the Jackpot!")
            print("You won $"+betmoney*2)
            print(f"Your total now is {money}")
        elif len(duplicates)==1:
            print("You won!")
            print("You won $"+betmoney)
            print(f"Your total now is {money}")
        else:
            print("You lost...")
            print("You lost $"+betmoney)
            money = money-betmoney
            print(f"Your total now is {money}")
        yn1 = ("Play again?(y/n)\n>")
        if yn1=="y":
            start()
        if yn1=="n":
            print("Bye, game ends here.")

    game(0)
    game(1)
    game(2)
    check()
def bettingphase():
    print(f"{user}:You have ${money}")
    global betmoney 
    betmoney = int(input("How much money you want to bet?\n>$"))

def start():
    bettingphase()
    yn = str(input(f"Confirm:${betmoney}?(y/n)\n>"))
    if yn=="y":
        print("Game starting, redirecting...")
        gamestart()
    elif yn=="n":bettingphase()
    
print("Welcome to Slot")
time.sleep(1)
user = str(input("Username:"))
print("The rules of this game are simple: Spin the wheel a number of times to get a number; get the 3 same numbers in a row and you win!")
time.sleep(3)
money = 1000
start()
    

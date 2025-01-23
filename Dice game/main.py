import random

count=0
while True:
    choice=input("Are you ready to play (Y/N): ").lower()
    if(choice=='y'):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1}, {die2})")
        count+=1
    elif(choice=='n'):
        print("Thanks for playing!!")
        print(f'You have rolled dice {count} Times')
        break
    else:
        print("Invalid choice")

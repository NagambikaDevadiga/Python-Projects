import random

while True:
    choice=input("Are you ready to play (Y/N): ").lower()
    if(choice=='y'):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1}, {die2})")
    elif(choice=='n'):
        print("Thanks for playing!!")
        break
    else:
        print("Invalid choice")

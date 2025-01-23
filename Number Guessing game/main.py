import random

random_num=random.randint(1,100)
n=-1
guesses=1
while(n!=random_num):
    n=int(input("Guess the number: "))
    if(n>random_num):
        print("Lower number please!")
        guesses+=1

    elif(n<random_num):
        print("Higher number please")
        guesses+=1

print(f"You guessed the number {random_num} in {guesses} attempts!!")
    


import random
secret = random(1,50)
hearts = 5
guess = int(input("what number do you guess"))

while hearts: 
    if guess == secret:
        print("wow you got it")
    else:
        
  
    if guess == secret:
        print("wow you got it")
    else:
        print("you did not get it")

    if guess > secret:
        print("hmm its greater the secret number")
    else:
        print("hmm its lesser than the secret number")


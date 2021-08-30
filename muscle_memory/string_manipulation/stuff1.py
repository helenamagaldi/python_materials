import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0 

while guess != int(n * random.random()) + 1:
    guess = int(input("New nyumber"))
    
    if guess > to_be_guessed:
        print("Number too large")
    elif guess < to_be_guessed:
        print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulations, you made it!")

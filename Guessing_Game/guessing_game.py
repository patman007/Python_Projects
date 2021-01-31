#Import Random Library/Module to as variable r
import random as r

#Num variable will randomly generate random number between 0 and 100
num = r. randrange(100)

#Count variable for decrementing the value
Guess = 5

#WHILE LOOP for Guess variable
while Guess >= 0:
    #Input from user
    your_guess = int(input('Enter your Guess: '))

    #Defined Function called Check inside While Loop
    def check(x):
        if your_guess == x:
            print('you win')
        elif your_guess > x:
            print('You are close, keep trying lower')
        else:
            print('Your are close, keep trying higher')

    #Guess iteration countdown for your fie chances
    if Guess > 1:
        check(num)
    elif Guess == 1:
        check(num)
        print('This is your LAST chance, make the most of it')
    else:
        print('you lost')
    Guess = Guess - 1


#This is a guess the number game

import random
print('Im thinking of a number better 1 and 20')
secretNumber = random.randint(1,20)

#6 guesses
for guessesTaken in range(1,7):
    print('take a guess')
    try:
        guess = int(input())
    except SyntaxError:
        print('enter a number between 1 - 20 please')
    

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break #loop breaks and continues when guess is correct

if guess == secretNumber:
    print('Nice you got it in ' + str(guessesTaken) + ' guesses') 
else:
    print('nope the number was ' + str(secretNumber))

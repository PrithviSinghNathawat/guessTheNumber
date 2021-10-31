import random
print('GUESS THE NUMBER')
rnumber=random.randint(1,9)
chances=0
print('Guess the number between 1 to 9-> ')
while chances <5:
    uInput=int(input('enter  your number: '))
    if uInput==rnumber:
        print('Congratulations YOU WON!!!')
        break
    elif uInput<rnumber:
        print('your guess was too low!')
    else:
        print('your guess was too high!')
    chances=chances+1
if not chances<5:
    print('Better luck next time! ;(')

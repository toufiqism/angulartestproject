import random

randint = random.randint(1, 15)

for i in range(0, 7):
    print('Guess My Number')
    intx = int(input())
    if intx < randint:
        print('Your Guess is too low')
    elif intx > randint:
        print('Your Guess is too high')
    else:
        break

if intx == randint:
    print('Congratulations, You have guessed correctly in', i+1, 'tries')
else:
    print('Nope, my number was ', randint)

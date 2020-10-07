import random

ints = range(33,127)
password =''

for i in range(16):
    password += chr(random.choice(ints))

print(f'password is: {password}')

#zadanie rzut kostka

min = 1
max = 6

dices = []

print(dices)

for i in range(5):
    dice = random.randint(min, max)

    if dice == 1:
        dices.append(print('o'))
    elif dice == 2:
        dices.append(print('o o'))
    elif dice == 3:
        dices.append(print('   o\n  o\n o'))
    elif dice == 4:
        dices.append(print('o o\no o'))
    elif dice == 5:
        dices.append(print('o   o\n  o\no   o'))
    else:
        dices.append(print('o o\no o\no o'))



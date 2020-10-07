#zadanie 1
import random


for i in range(1,11):
    print(i,random.randrange(1,100))

number1 = random.randrange(1,100)
counter = 1

while True:
    number2 = random.randrange(1,100)
    print(f'number1: {number1} number2:{number2}')
    if number2 == number1:
        print(f'number1:{number1} = number2:{number2}')
        break
    else:
        counter+=1
print(f'tries:{counter}')

#zadanie 2

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print(f'------Group {groupNumber}------')
    print(countries[i])


for number in range(1,21):
    if number % 2 == 0:
        print('number %2d is %s' % (number,'even'))
    else:
        print('number %2d is %s' % (number,'odd'))

#zadanie 1

string_a = '+-----+----+-----+'
string_b = '|     |    |     |'

for i in range(1,6):
    print(string_a)
    print(string_b)
else:
    print(string_a)

#zadanie 2

for i in range(1,6):
    print('x'*i)

#zadanie 3

for i in range(1,6):
    if i % 2 ==0:
        print('x'*i)
    else:
        print('o'*i)
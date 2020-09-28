somethingLikeNumber='1000'
print(somethingLikeNumber)
print(somethingLikeNumber + '1')
print(int(somethingLikeNumber) + 1)
print(somethingLikeNumber+ str(1))

print('----------------')
# zadanie 1, 2 i 3

article = '''Monty Python, grupa Monty Pythona, Pythoni – zespół twórców i gwiazd telewizyjnego serialu komediowego 
Latający cyrk Monty Pythona, założony pod koniec lat 60. XX wieku w Anglii. 
W skład grupy wchodziło sześciu komików: Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones i Michael Palin.
'''
print(article.upper())

#zadanie 4

print(article.lower().replace('monty', 'python'))

#zadanie 5

print(article.lower().split(" "))

#zadanie 6

print('word python appears', article.lower().count('python'), 'times')

#zadanie 7

print('to print \\ you need to put \\ twice in your text \nlike this: \\\\')

#zadanie 8

print("'the best hits of 80\'s!!!'")
print('"the best hits of 80\'s!!!"')

#zadanie 9

PLN = 234
USD = 3.65
EUR = 4.23

print('cur\texchange\tamount')
print(f'USD\t{USD}\t{PLN/USD}')
print(F'EUR\t{EUR}\t{PLN/EUR}')

#zadanie 10

ValueAsText = '123.45'
factor = 1.23
print(f'value is {ValueAsText} factor is {factor} value*factor= {float(ValueAsText) * factor} ')
text='this is text'
#czy tekst jest z duzych liter?
print(text.isupper())

#czy text jest z małyh liter?
print(text.islower())

#czy text jest liczba?
print(text.isdigit())

#czy text jest liczba zmiennoprzecinkowa?
print(text.isdecimal())

#czy text jest literami?
print(text.isalpha())

#czy text jest liczbami i literami?
print(text.isalnum())

print('------------------------')

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street.'

print('------------------------')
print(quote.upper())
print('------------------------')
print(quote.lower())
print('------------------------')
print(quote.endswith("street"))
print('------------------------')
print(quote.isupper())
print('------------------------')
print(quote.upper().isupper())
print('------------------------')
print(quote.find('one'))
print('------------------------')
print(quote.replace('one', "1"))
print('------------------------')
print(quote.replace('one', '1').replace('both', '2'))
print('------------------------')
print(quote.split(" "))

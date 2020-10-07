persons=['elizabeth','steven','sebastian','margaret','stevlana','raphel']
domain = 'mycompany.com'
for person in persons:
    email = person + '@' + domain
    print('email for \t', person, '\tis\t', email)
else:
    print('---end of the list---')

#zadanie 1

data = ['error: file cannot be open',
        'error: no free space on disk',
        'error: file missing',
        'warning: internet conection lost',
        'error:acces denied']

for error in data:
    elements = error.split(":")
    if elements[0] == 'error':
        print(elements[0], elements[1].upper())
    else:
        print(elements[0], elements[1])
else:
    print('end of the list!!!!!!')
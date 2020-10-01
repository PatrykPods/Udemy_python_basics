countryLeaders={'pl': 'duda', 'us' : 'trump'}

countryLeaders['de'] = 'merkel'
#print(countryLeaders)
#print(countryLeaders.keys())
#print(countryLeaders.values())
#print(countryLeaders.items())

#print(countryLeaders.popitem())

#print(countryLeaders.setdefault('fr', 'macron'))
#print(countryLeaders.get('ru'))

newLeaders = {'ru':'putin', 'de':'dchulz'}
countryLeaders.update(newLeaders)
print(countryLeaders)

#zadanie 1 i 2

chanels = {'google': 1480, 'email':300, 'natural traffic':440, 'tv spot':700}
print(chanels['email'])

#zadanie 3,4 i 5

chanelsUpdate = {'natural traffic':520, 'news':600}
chanels.update(chanelsUpdate)
print(chanels)

chanels.pop('email')

print(chanels)

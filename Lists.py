countries = ['fr','us','de','ru']
countries[1] = 'gb'
print(countries[1])
countries.append('pl')
countries.insert(2,'es')
countries.remove('ru')
countries.sort()
print(countries)
countries.reverse()
print(countries.pop(2))
print(countries.index('pl'))
print(countries.count('de'))

newlist = ['fi', 'se']

countries.extend(newlist)
print(countries)

countriescopy = countries.copy
print(countriescopy())
countriescopy().clear()
print(countriescopy())

#Zadania 1-

hitsTitles = ['brothers in arms', 'bohemian rhapsody', 'stairways to heaven', 'wish you were here']
hitsTitles.append('child in time')
hitsTitles.append('again')
hitsTitles.insert(2,'hotel california')
hitsTitles.insert(0,'the sounds of silence')
print('hotel california is on position:', hitsTitles.index('hotel california')+1)
hitsTitles.remove('hotel california')
hitsTitles[0] = 'enjoy the silence'
print(hitsTitles)

hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print(hitsToRead)

aditionalSongs = ['nothing compares 2 you', 'wish you were here']
hitsToRead.extend(aditionalSongs)
print(hitsToRead)
print(f'wish you were here will be played:', hitsToRead.count('wish you were here'), ' times, and riders on the storm will be played:', hitsToRead.count('riders on the storm'),'times')

age = 21
isDrunk = False
isRestrictedArea = False

if age < 18:
    print('You are to young')
elif isDrunk:
    print('you are drunk, we cannot sell you alcohol')
elif isRestrictedArea:
    print("alcohol is forbiden")
else:
    print('you can buy alcohol')

#zadanie 1

min_shares = 500
min_likes = 100

num_of_likes = 120
num_of_shares = 700

if num_of_shares < min_shares and num_of_likes < min_likes:
    print('not enough shares and likes')
elif num_of_likes < min_likes:
    print('not enough likes')
elif num_of_shares < min_shares:
    print('not enough shares')
else:
    print('10% discount')

#zadanie 2

ispizzaordered = False
isBigDrinkordered = False
isWeekend = False

if not isWeekend and (ispizzaordered or isBigDrinkordered):
    print('free burger!')
elif isWeekend:
    print('to get free burger order pizza or big dring during work days')
else:
    print('to get free burger order pizza or big drink')
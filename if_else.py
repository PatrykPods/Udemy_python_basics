age = 23

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print('you are to young to buy alcohol')

isDrunk = False

if age >= 18 and not isDrunk:
    print('You are adult and you can buy alcohol')
else:
    print('sorry, we cannot sell you alcohol')

isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print('you can buy alcohol')
else:
    print('we cannot sell you alcohol')

#zadanie 1

min_likes = 500
min_shares = 100

num_of_likes = 1300
num_of_shares = 70

if num_of_likes >= min_likes and num_of_shares >= min_shares:
    print('discount 10%')
else:
    print('not enough shares and likes')

#zadanie 2

isPizzaOrdered = True
isBigDrinkOrderes = False
isWeekend = False

if not isWeekend and (isBigDrinkOrderes or isPizzaOrdered):
    print('free burger!!!')
else:
    print('Buy pizza or big drink during work days to get free burger')

#zadanie 3

diskSize = 140
diskSizeUsed = 119
fileSize = 21

if fileSize <= diskSize - diskSizeUsed:
    print('You can download file')
else:
    print('not enough space on disk')
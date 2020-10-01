itRains = True

if itRains:
    print('we stay at home')
else:
    print('we go out')

print('we stay at home' if itRains else 'we go')

#zadanie 1,2 i 3

musclePain = True
fever = True
weakness = False

print('suspicion of influenza' if musclePain and fever and weakness else 'The flu is unlikely')

if musclePain and fever and weakness:
    print('suspicion of influenza')
elif not (musclePain and fever) and weakness:
    print('just take a rest')
else:
    print('you may be cold')

#zadanie 4 i 5

isMan = False
musclePain = False
fever = True
weakness = False


if musclePain and fever and weakness:
    print('suspicion of influenza')
elif not (musclePain and fever) and weakness and not isMan:
    print('just take a rest')
elif isMan and (musclePain or fever or weakness):
    print('suspicion of influenza')
else:
    print('you may be cold')

#zadanie 6
isCheckCompleted = False
print('check is completed' if isCheckCompleted else 'check not done yet')
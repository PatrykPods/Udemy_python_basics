IsWeekend = False
print('is weekend =', IsWeekend)

Temperature = 25
print('temperature =', Temperature)

ToDoList = ''
print('ToDoList=',ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList ==''
print('IsHappy =', IsHappy)

IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ''
print('IsHappy =', IsHappy)

#zadanie 1
isAutomaticMode = False
is80PercentLight = True
IsDirectLight = False
isRainy = True

turnLightsOn = isAutomaticMode and (not is80PercentLight or IsDirectLight or isRainy)

print('automatic mode:',isAutomaticMode)
print('Is the light good:',is80PercentLight)
print('is sun low:', IsDirectLight)
print('is it rainy:',isRainy)
print('TURN LIGHTS ON:',turnLightsOn)

#zadanie 2

obecnosc = 0.85
srednia = 3.5
praca = False

zaliczyl = obecnosc >= 0.8 and srednia >= 3 and praca == True
print('zaliczyl:',zaliczyl)
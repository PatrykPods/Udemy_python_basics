import sys
print(sys.maxsize)

five = 5
three = 3

print(five/three)
print(five//three)
print(five % three)

print(float('inf') > 9999999999999999999999999999999)

#zadanie 1,2,3 i 4

name = 'Patryk'
age = 26
DaysInYear = 365

message = f'{name} is {age} years old, so is about {age * DaysInYear} days old '
print(message)

#zadanie 5,6 i 7

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*DaysInYear ))

#zadanie 8
name = 'chris'
age = 17
DaysInYear = 365
message = '{0:s} is {1:d} years old, so is about {2:d}'
print(message.format(name, age, age*DaysInYear))

#zadanie 9

print(f'1234567890 divided by 12345 is {1234567890//12345} and the rest is {1234567890 % 12345}')
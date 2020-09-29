message1 = 'processing file %s'
print(message1 % ('file_1.txt'))

message2 = 'file %s has size %d KB'
print(message2 % ('file1_txt', 100))

message3 = 'file %20s has size %10d KB'
print(message2 % ('file1_txt', 100))

message4 = 'processing file{0:s}'
print(message4.format('file1_txt'))

message5 = 'file{0:s} has size{1:d}'
print(message5.format('file.txt', 100))

print('-----------------------------')

#zadanie 1 i 2

helloMessage = 'hello %s!'
print(helloMessage % "Kate")
print(helloMessage % "Chris")


#zadanie 3 i 4

hellomessage = 'Hello {0:s}!'
print(hellomessage.format('Chris'))
print(hellomessage.format('kate'))

#zadanie 5 i 6

helloMessage = '%s has %d %s'
print(helloMessage % ('kate', 1, 'animal'))
print(helloMessage % ('Chris', 100000, '$'))

#zadanie 7 i 8

helloMessage = '{0:s} has {1:d} {2:s}'
print(helloMessage.format('kate', 1, 'animal'))
print(helloMessage.format('chris', 1000000, '$'))

#zadanie 9 i 10

line = '%20s costs %6d €'
print(line % ('ice cream', 3))
print(line % ('trip to venice', 119))
print(line % ('pizza hawai', 6))

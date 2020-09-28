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




s='A python script'
print(s[0])
print(s[2])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:99999999])
print(s[222:9999])

message = 'document "cv.doc" was printed on printer: XEROX'
print(message[message.find(':')+2:])

print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

#zadanie 1 i 2

q = 'The eyes'
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])

#zadanie 3

q = 'a gentleman'
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])

#zadanie 4

q = 'THE MORSE CODE'
print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[11],q[0],q[7])

#zadanie 5

line = "'program \"pytanie na sniadanie\" nadamy o: 6:00"
print(line)

time = line[line.find(':')+1:]
print(time)

tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title)
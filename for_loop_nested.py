for x in range(1,11):
    line = str(x)
    for y in range(1,11):
        line += '\t'+ str(x*y)
    print(line)

#zadanie 1
i = 10
result = 1

for j in range(1,i+1):
    result*=j
    print(i,result)

#zadanie 2
x = 10

for i in range(1,x+1):
    result = 1
    for j in range(1,i+1):
        result*= j
    print(i, result)

#zadanie 3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful','fast']

for noun in list_noun:
    for adj in list_adj:
        print(noun + '-' + adj)
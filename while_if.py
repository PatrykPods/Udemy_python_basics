values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i = 0
max = len(values)-2

while i < max:

    if values[i]<values[i+1]<values[i+2]:
        print(values[i],values[i+1],values[i+2])
    i+=1
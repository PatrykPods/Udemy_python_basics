tax = (4,7,8,23)

print(tax[2])
print(tax[-1])
print(tax.index(7))
print(tax.count(8))
print(max(tax))

#tax.revert()
taxlist = list(tax)
taxlist.append(30)
newtax = tuple(taxlist)

print(tax)
print(taxlist)
print(newtax)

(tax1, tax2, tax3, tax4) = tax
print(tax1)
print(tax2)

a=1
b=10
print('a=',a,"\tb=",b)
#temp = a
#a=b
#b=temp

(a,b) = (b,a)
print('a=',a,"\tb=",b)

#zadania 1 - 9

marketing = ['loyality program', 'client promotion', 'market research']
marketing.append('public relations')
print(marketing[3])
marketing.insert(2,'investor relations')
emailmarketing = marketing.copy()
print(emailmarketing)
emailmarketing.sort()
internalemails = ['internal comunications']
emailmarketing.extend(internalemails)
print(emailmarketing)
tuple = tuple(emailmarketing)
print(tuple)


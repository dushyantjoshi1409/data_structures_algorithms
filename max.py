a = 'my name is'
b = a.split()
d = ''
for i in b:
    if i == 'is':
        d = i[::-1] + ' ' + d
    else:
        d = i + ' ' +  d
print(d)
a = [int(i) if i.isdigit() else [int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {i:[1 for j in range(n)] for i in ['rotated','not_rotated']}
for i in range(1,n):
    if a[i][0]==a[i-1][0]: d['not_rotated'][i] = d['rotated'][i-1]+1
    if a[i][0]==a[i-1][1]: d['not_rotated'][i] = d['not_rotated'][i-1]+1
    if a[i][1]==a[i-1][0]: d['rotated'][i] = d['rotated'][i-1]+1
    if a[i][1]==a[i-1][1]: d['rotated'][i] = d['not_rotated'][i-1]+1
print(max([max(d[i]) for i in d])) #19 235
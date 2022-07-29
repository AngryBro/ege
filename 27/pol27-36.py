from math import gcd
a = [int(i) if i.isdigit() else [int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[-float('inf') for i in range(n)] for j in range(10)}
for i in range(2):
    for j in range(i+1,3):
        nod = gcd(a[0][i],a[0][j])
        d[nod%10][0] = max(d[nod%10][0],nod)
for i in range(1,n):
    for j in range(10):
        for k in range(2):
            for l in range(k+1,3):
                nod = gcd(a[i][k],a[i][l])
                d[j][i] = max(d[j][i],d[(j-nod)%10][i-1]+nod)
print(d[0][n-1]) #110 519880
a = [int(i) if i.isdigit() else [int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[-float('inf') for i in range(n)] for j in range(7)}
for i in a[0]:
    d[i%7][0] = max(d[i%7][0],i)
for i in range(1,n):
    for j in range(7):
        for k in range(2):
            d[j][i] = max(d[j][i],d[(j-a[i][k])%7][i-1]+a[i][k])
print(d[sum([min(i) for i in a])%7][n-1]) #115110 410884352
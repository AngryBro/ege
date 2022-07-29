a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[0 for i in range(n)] for j in (list(range(14))+['count'])}
d[a[0]%14][0] = 1
for i in range(1,n):
    for j in range(14):
        d[j][i]=d[j][i-1]+int(a[i]%14==j)
    if i>=5: d['count'][i] = d[(-a[i])%14][i-5]
print(sum(d['count'])) #8 128567918
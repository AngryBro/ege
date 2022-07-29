a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {k:{j:[-float('inf') for i in range(n)] for j in range(3)} for k in [1,2,3]}
d[1][a[0]%3][0] = a[0]
for i in range(1,n):
    for j in range(3):
        d[1][j][i] = max(d[1][j][i-1],a[i] if a[i]%3==j else -float('inf'))
        for k in [2,3]:
            d[k][j][i] = max(d[k][j][i-1],d[k-1][(j-a[i])%3][i-1]+a[i])
print(d[3][0][n-1]) #2919 299988174
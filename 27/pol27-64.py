a = [sorted([int(j) for j in i.split()]) for i in open(input()+'.txt').read().splitlines() if int(i.split()[0])%2!=0 and not i.isdigit()]
n = len(a)
d = [[[-float('inf') for i in range(n)] for j in range(2)] for k in range(2)]
d[a[0][0]%2][a[0][1]%2][0] = sum(a[0])
for i in range(1,n):
    d[a[i][0]%2][a[i][1]%2][i] = sum(a[i])
    for j in range(2):
        for k in range(2):
            d[j][k][i] = max(d[j][k][i-1],d[j][k][i], sum(a[i])+d[(j+a[i][0])%2][(k+a[i][1])%2][i-1])
print(d[0][1][n-1]) #78931 314825807
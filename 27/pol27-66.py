a = [[int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n=a.pop(0)[0]
d = [[[-float('inf') for i in range(n)] for j in range(5)] for k in range(3)]
d[a[0][0]%3][a[0][1]%5][0]=a[0][1]
d[a[0][1]%3][a[0][0]%5][0]=max(a[0][0],d[a[0][1]%3][a[0][0]%5][0])
for i in range(1,n):
    for l in range(2):
        for k in range(3):
            for j in range(5):
                d[k][j][i]=max(d[k][j][i],d[(k-a[i][l])%3][(j-a[i][l])%5][i-1]+a[i][l])
e = []
for j in range(1,5):
    for k in range(1,3):
        e.append(d[k][j][n-1])
print(max(e)) #454 3695118
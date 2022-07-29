a = [int(i) if i.isdigit() else [int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = [[-float('inf') for i in range(n)] for digit in range(10)]
for i in a[0]: d[i%10][0] = max(d[i%10][0],i)
for i in range(1,n):
    for j in range(10):
        for aik in a[i]:
            d[j][i] = max(d[(j-aik)%10][i-1]+aik,d[j][i])
print(d[8][n-1]) #13608 40724928
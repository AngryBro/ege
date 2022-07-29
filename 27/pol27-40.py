a = [int(i) if i.isdigit() else [int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[-float('inf') for i in range(n)] for j in range(2)}
for i in a[0]: d[i%2][0] = max(d[i%2][0],i)
for i in range(1,n):
    for j in range(2):
        for k in a[i]:
            d[j][i] = max(d[j][i],d[(j-k)%2][i-1]+k)
print(d[0][n-1] if sum([sum(i) for i in a])%2==0 else d[1][n-1]) #621 103914584
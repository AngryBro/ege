a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[0 for i in range(n)] for j in range(3)}
d[a[0]%3][0] = 1
for i in range(1,n):
    for j in range(3):
        d[j][i] = d[(j-a[i])%3][i-1]+d[j][i-1] + (1 if a[i]%3==j else 0)
print(d[0][n-1]) #351 357914111
a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n=a.pop(0)
d = {j:[1 for i in range(n)] for j in range(1,101)}
a.sort()
index = {a[i]:i for i in range(n)}
for i in range(1,n):
    for j in range(1,101):
        if a[i]-j in index:
            d[j][i]=d[j][index[a[i]-j]]+1
print(max([max(d[i]) for i in d])) #5 317

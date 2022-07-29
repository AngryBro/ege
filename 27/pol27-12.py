a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
divs = [6,3,2]
d = {j:[0 for i in range(n)] for j in ['count']+divs}
if a[0]%6==0: d[6][0] = 1
elif a[0]%3==0: d[3][0] = 1
elif a[0]%2==0: d[2][0] =1
for i in range(1,n):
    k=0
    for j in divs:
        if a[i]%j==0: 
            k=j
            d[k][i]=d[k][i-1]+1
            break
    for j in divs:
        if k!=j: d[j][i]=d[j][i-1]
        if a[i]%6==0: d['count'][i]=i
        elif a[i]%3==0: d['count'][i]=d[2][i-1]+d[6][i-1]
        elif a[i]%2==0: d['count'][i]=d[3][i-1]+d[6][i-1]
        else: d['count'][i]=d[6][i-1]
print(sum(d['count'])) #47 745460178
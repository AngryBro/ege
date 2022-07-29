a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[float('inf') if j=='-' else -float('inf') for i in range(n)] for j in ['+','-']}
if a[0]>=0: d['+'][0]=a[0]
else: d['-'][0] = a[0]
for i in range(1,n):
    if a[i]!=0:
        d['+' if a[i]<0 else '-'][i]=d['-'][i-1]*a[i]
        d['+' if a[i]>0 else '-'][i]=max(1,d['+'][i-1])*a[i]
    else:
        d['+'][i]=0
print(max(d['+'])) #663497670 999806976
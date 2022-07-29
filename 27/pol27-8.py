a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[float('inf') for i in range(n)] for j in ['min_sqr','min_sum']}
d['min_sqr'][0] = a[0]**2
for i in range(1,n):
    d['min_sqr'][i] = min(a[i]**2,d['min_sqr'][i-1])
    if i>=5: d['min_sum'][i] = a[i]**2+d['min_sqr'][i-5]
print(min(d['min_sum'])) #11009 200
c2 = sum([i*a[i] for i in a])
c1 = sum([a[i] for i in a])
m = float('inf')
indexes = list(a.keys())[::-1]
sum1 = 0
sum2 = 0
for j in indexes:
    sum1 += j*a[j]
    sum2 += a[j]
    t = j*c1+2*(sum1-j*sum2)
    m = min(m,t)
print(m-c2)
#51063 5634689219329
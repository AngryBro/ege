a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[float('inf') for i in range(n)] for j in ['odd','mult']}
if a[0]%2!=0: d['odd'][0] = a[0]
for i in range(1,n):
    d['odd'][i] = min(a[i],d['odd'][i-1]) if a[i]%2!=0 else d['odd'][i-1]
    if a[i]%2!=0 and i>=6: d['mult'][i] = d['odd'][i-6]*a[i]
print( min(d['mult']) if min(d['mult'])!=float('inf') else -1 ) #2465 121 
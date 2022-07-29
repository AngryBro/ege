a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {j:[0 for i in range(n)] for j in ['+2+13','+2-13','-2+13','-2-13','pairs']}
d[('+' if a[0]%2==0 else '-')+'2'+('+' if a[0]%13==0 else '-')+'13'][0] = 1
for i in range(1,n):
    d['+2+13'][i] = d['+2+13'][i-1] + int(a[i]%13==0 and a[i]%2==0)
    d['-2+13'][i] = d['-2+13'][i-1] + int(a[i]%13==0 and a[i]%2!=0)
    d['+2-13'][i] = d['+2-13'][i-1] + int(a[i]%13!=0 and a[i]%2==0)
    d['-2-13'][i] = d['-2-13'][i-1] + int(a[i]%13!=0 and a[i]%2!=0)
    if i>=5:
        if a[i]%13==0 and a[i]%2==0: d['pairs'][i] = d['-2+13'][i-5]+d['-2-13'][i-5]
        if a[i]%13==0 and a[i]%2!=0: d['pairs'][i] = d['+2+13'][i-5]+d['+2-13'][i-5]
        if a[i]%13!=0 and a[i]%2==0: d['pairs'][i] = d['-2+13'][i-5]
        if a[i]%13!=0 and a[i]%2!=0: d['pairs'][i] = d['+2+13'][i-5]
print(sum(d['pairs'])) #6 129920689
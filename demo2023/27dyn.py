a = [[int(j) for j in i.split()] for i in open('27_'+input()+'.txt').read().splitlines()]
a.pop(0)
a = {i[0]:i[1]//36 + (1 if i[1]%36 else 0) for i in a}
n = max(a.keys())
d = {j:[None for i in range(n+1)] for j in ['sum-','sum+','sum']}
d['sum-'][0] = 0
d['sum+'][0] = sum([a[i] for i in a if i!=0])
d['sum'][0] = sum([a[i]*i for i in a])
for i in range(1,n+1):
    d['sum-'][i] = d['sum-'][i-1]+(a[i-1] if i-1 in a else 0)
    d['sum+'][i] = d['sum+'][i-1]-(a[i] if i in a else 0)
    d['sum'][i] = d['sum'][i-1]+d['sum-'][i]-d['sum+'][i-1]
print(min([d['sum'][i] for i in a]))
#51063 5634689219329
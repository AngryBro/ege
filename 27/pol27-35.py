a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
d = {name:[0 for i in range(n)] for name in ['odd_0','even_0','even_all','odd_all','count']}
if a[0]>0: d['even_all' if a[0]%2==0 else 'odd_all'][0] = 1
for i in range(1,n):
    if a[i]==0:
        for name in ['even_all','odd_all']: d[name][i] = d[name][i-1]
        d['even_0'][i] = d['even_all'][i-1]
        d['odd_0'][i] = d['odd_all'][i-1]
    if a[i]>0:
        for name in ['even_0','odd_0']: d[name][i] = d[name][i-1]
        d['even_all'][i] = d['even_all'][i-1]+int(a[i]%2==0)
        d['odd_all'][i] = d['odd_all'][i-1]+int(a[i]%2!=0)
        d['count'][i] = d['even_0'][i-1] if a[i]%2==0 else d['odd_0'][i-1]
print(sum(d['count'])) #51 24019058
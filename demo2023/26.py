a = [int(i) for i in open('26.txt').read().splitlines()]
#a = [5,43,40,32,40,30]
n = a.pop(0)
a.sort(reverse = 1)
b = [a.pop(0)]
for i in range(n-1):
    if b[-1]-a[0]>=3:
        b.append(a.pop(0))
    else: a.pop(0)
print(len(b),b[-1]) #2767 51
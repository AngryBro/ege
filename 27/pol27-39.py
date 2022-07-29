a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
b = [0 for i in range(1000)]
for i in range(n):
    b[a[i]]+=1
max_pal = 0
for i in range(100,len(b)):
    if str(i)!=str(i)[::-1]: b[i] = min(b[i],b[int(str(i)[::-1])])
    elif b[i]%2!=0: max_pal = max(max_pal,i)
for i in range(100,len(b)):
    if str(i)==str(i)[::-1] and b[i]%2!=0 and i<max_pal:
        b[i]-=1
number = ''
for i in range(100,len(b)):
    number += str(i)*b[i]
print(sum([int(i) for i in number])) #75 508801
a = [int(i) for i in open('17.txt').read().splitlines()]
m = -float('inf')
k = 0
maxsqr = -float('inf')
for i in a:
    if abs(i)%10==3 and i>m: m = i
for i in range(len(a)-1):
    end1 = abs(a[i])%10
    end2 = abs(a[i+1])%10
    sumsqr = a[i]**2 + a[i+1]**2
    if (end1==3 or end2==3) and end1+end2!=6 and sumsqr>=m**2:
        k+=1
        if sumsqr>maxsqr: maxsqr = sumsqr
print(k,maxsqr) #180 190360573
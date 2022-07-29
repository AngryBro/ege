a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
top = {i:[] for i in range(3)}
for i in a:
    top[i%3]+=[i]
for i in top:
    top[i].sort(reverse=1)
var1 = 0
if len(top[0])*len(top[1])*len(top[2])!=0:
    for i in top:
        var1 += top[i][0]
else: var1 = -float('inf')
var2 = 0
for i in top:
    if len(top[i])>2:
        var2 = max(var2, top[i][0]+top[i][1]+top[i][2])
print(max(var1,var2)) #2919 299988174
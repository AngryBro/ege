a = [[int(j) for j in i.split(';')] for i in open('9.csv').read().splitlines()]
count = 0
for i in a:
    k = 0
    for j in i:
        k += i.count(j)
    if k!=8: continue
    for j in i:
        if i.count(j)==2:
            e = j
    if (sum(i)-2*e)/4 <= 2*e: count+=1
print(count) #2241
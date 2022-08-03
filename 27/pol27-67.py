def groups(array):
    if len(array)==1: return [array]
    e = array.pop()
    last = groups(array)
    news = []
    for i in last:
        news.append(i.copy()+[e])
    last.append([e])
    last += news
    return last
a = [[int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)[0]
d = [[-float('inf') for i in range(n)] for j in range(5)]
for i in range(n): 
    a[i].pop(0)
    a[i] = [sum(j) for j in groups(a[i]) if sum(j)%2==0]
for s in a[0]: d[s%5][0] = max(d[s%5][0],s)
for i in range(1,n):
    for j in range(5):
        for s in a[i]:
            d[j][i] = max(d[j][i], d[(j-s)%5][i-1]+s)
print(max([d[j][n-1] for j in range(1,5)])) #4908 134271196
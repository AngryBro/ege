sogl = ['C','D','F']
gl = ['A','O']
s = open('24.txt').read()
n = len(s)
d = [0 for i in range(n)]
if s[1] in gl and s[0] in sogl: d[1] = 1
for i in range(2,n):
    if s[i] in gl and s[i-1] in sogl:
        d[i] = d[i-2]+1
print(max(d)) #95
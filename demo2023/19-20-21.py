def strategy19(s,i):
    m = 129
    yes = i==2 and s>=m
    no = i<2 and s>=m or i==2 and s<m
    if yes: return 1
    if no: return 0
    if i==0: return strategy19(s+1, i+1) and strategy19(s*2, i+1)
    if i==1: return strategy19(s+1, i+1) or strategy19(s*2, i+1)

def strategy20(s,i):
    m = 129
    yes = i==3 and s>=m
    no = i<3 and s>=m or i==3 and s<m
    if yes: return 1
    if no: return 0
    if i%2==0: return strategy20(s+1, i+1) or strategy20(s*2, i+1)
    if i%2!=0: return strategy20(s+1, i+1) and strategy20(s*2, i+1)
def strategy21_2(s,i):
    m = 129
    yes = (i==4 or i==2) and s>=m
    no = i%2 and s>=m or i==4 and s<m
    if yes: return 1
    if no: return 0
    if i%2: return strategy21_2(s+1, i+1) or strategy21_2(s*2, i+1)
    if not i%2: return strategy21_2(s+1, i+1) and strategy21_2(s*2, i+1)
def strategy21_1(s,i):
    m = 129
    yes = i==2 and s>=m
    no = i%2 and s>=m or i==2 and s<m
    if yes: return 1
    if no: return 0
    if i%2: return strategy21_1(s+1, i+1) or strategy21_1(s*2, i+1)
    if not i%2: return strategy21_1(s+1, i+1) and strategy21_1(s*2, i+1)
#19
for s in range(1,129):
    if strategy19(s, 0): print('19:',s)
#20
ans20 = []
for s in range(1,129):
    if strategy20(s, 0): ans20.append(s)
print('20:',ans20[0],ans20[1])
#21
ans21 = []
for s in range(1,129):
    if strategy21_2(s, 0) and not strategy21_1(s, 0):
        ans21.append(s)
print('21:',min(ans21))

# 19: 64
# 20: 32 63
# 21: 62
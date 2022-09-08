import re
m = bool(re.fullmatch('123\d*4\d?5', '12300405'))
for i in range(1,10**10):
    if i*2023>10**10: break
    if re.fullmatch('1\d2139\d*4', str(2023*i)):
        print(2023*i,i)
# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048
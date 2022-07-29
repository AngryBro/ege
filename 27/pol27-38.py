a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
digits = {j:0 for j in range(10)}
for i in a:
    digits[i]+=1
max_odd = 0
for i in digits:
    if digits[i]%2!=0: max_odd = i
for i in range(max_odd):
    if digits[i]%2!=0: digits[i]-=1
s = 0
for i in digits: s += digits[i]*i
print(s) #71 254363

#дибильная задача
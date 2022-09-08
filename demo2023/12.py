def alg(s):
    while '>1' in s or '>0' in s or '>2' in s:
        if '>1' in s: s = s.replace('>1','22>',1)
        if '>2' in s: s = s.replace('>2','2>',1)
        if '>0' in s: s = s.replace('>0','1>',1)
    return s
def prime(x):
    for i in range(2,x):
        if i*i>x: break
        if x%i==0: return 0
    return 1
def sumstr(s):
    return sum([int(i) for i in s if i.isdigit()])
def main(n):
    s = '>'+'02'*39+'1'*n
    return prime(sumstr(alg(s)))

for n in range(1,100):
    if main(n):
        print(n)
        break
#5
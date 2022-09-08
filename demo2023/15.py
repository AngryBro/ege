def DEL(n,m): return n%m==0
def f(x,A):
    return not DEL(x,2) or not DEL(x,3) or A+x>=100

for A in range(1,100):
    flag = 1
    for x in range(1,100):
        if not f(x,A): flag = 0
    if flag:
        print(A)
        break
#94
def f(x): return int('123'+x+'5',15)+int('1'+x+'233',15)

for x in '0123456789ABCDE':
    if f(x)%14==0:
        print(f(x)//14)
        break
#8767
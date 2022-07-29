a = [int(i) if i.isdigit() else [int(j) for j in i.split()] for i in open(input()+'.txt').read().splitlines()]
n = a.pop(0)
#hz
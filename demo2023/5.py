def alg(N):
    N2 = bin(N)[2:]
    if(N2.count('1')%2==0):
        R = '10'+N2[2:]+'0'
    else:
        R = '11'+N2[2:]+'1'
    return int(R,2)


for N in range(1,100):
    if(alg(N)>40):
        print(N)
        break
#16
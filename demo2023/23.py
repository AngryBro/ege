def programs(functions,numbers,no = []):
    def simplePrograms(start,number,functions,no):
        d = {i:0 for i in range(start,number+1)}
        d[start] = 1
        for i in range(start,number+1):
            if i in no: d[i] = 0
            for f in functions:
                if f(i)<=number:
                    d[f(i)] += d[i]
        return d[number]
    k = 1
    for i in range(len(numbers)-1):
        k *= simplePrograms(numbers[i],numbers[i+1], functions, no)
    return k

print(programs([lambda x: x+1,lambda x: x*2], [1,10,35],[17]))

#98


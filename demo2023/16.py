def f(n):
    d = [None for i in range(2024)]
    d[1] = 1
    for i in range(2,2024):
        d[i] = i*d[i-1]
    return d[n]
print(f(2023)/f(2020))
#8266912626
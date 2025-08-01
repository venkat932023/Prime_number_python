def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    else:
        return 1
    
n = int(input())
m = n+1
while True:
    if prime(m) == 1:
        print(m)
        break
    m=m+1
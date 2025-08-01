def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
    
n = int(input())
m = int(input())
i = n
j = n+2
while j<=m:
    if prime(i)  and prime(j):
        print(i,j)
    i+=1
    j=i+2
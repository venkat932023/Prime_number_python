def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    else:
        return 1

n = int(input())
a,b = 0,1
l = []
for i in range(1,n+1):
    l.append(a)
    a,b = b,a+b
for i in range(len(l)):
    if prime(l[i]) == 1:
        print(l[i],end=" ")

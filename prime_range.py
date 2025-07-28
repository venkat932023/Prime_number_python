# PRIME NUMBER IN RANGE OF 0 TO N

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

n = int(input())
for i in range(0,n+1):
    if prime(i)==1:
        print(i,end=" ")
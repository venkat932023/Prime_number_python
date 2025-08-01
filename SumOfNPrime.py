def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1

n = int(input())
i = 0
j = 2
s = 0

while i<n:
    if prime(j)==1:
        s+=j
        i+=1
    j+=1
print(s)
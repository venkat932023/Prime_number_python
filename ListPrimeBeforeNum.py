#List of prime number before number

def prime(n):
    if n <= 1:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    else:
        return 1

n = int(input())
l = []
for i in range(1,n):
    if n%i==0:
        if prime(i)==1:
            l.append(i)
print(max(l),min(l))
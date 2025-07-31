

def prime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1


n = int(input())
sum = 0
for i in str(n):
    sum += int(i)
if prime(sum) == 1:
    print("prime")
else:
    print("not prime")
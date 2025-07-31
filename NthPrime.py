#TO FIND Nth PRIME NUMBER

def prime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1


n = int(input())
k = 0
i = 0
while True:
    if prime(i) == 1:
        k+=1
    if n==k:
        print(i)
        break
    i+=1
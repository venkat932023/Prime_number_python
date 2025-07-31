#PRIME NUMBER SUM IN B/W RANGE

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    else:
        return 1





a = int(input())
b = int(input())

sum = 0
for i in range(a,b+1):
    if prime(i) == 1:
        sum+=i
print(sum)
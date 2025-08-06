def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    else:
        return 1
    
n = int(input())
r = n
l = len(str(n))
c = 0
for i in range(l):
    if prime(int(r))==1:
        c+=1
        print(r)
    r = str(r)[1:]+str(r)[0]
if c == l:
    print("Circular prime number")
else:
    print("not circular prime number")
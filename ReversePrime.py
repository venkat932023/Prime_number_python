# Reverse the given number and check if reversed number is prime or not if I/P is 13 the reverse number 31 is prime

n = int(input())
m = int(str(n)[::-1])
for i in range(2,m):
    if m%i == 0:
        print(m," Not prime")
        break
else:
    print(m," Prime")

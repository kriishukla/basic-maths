import math
n=int(input())
k=0
m=1
while n>=9:
    k=k+n%10*(10**(math.floor(math.log10(n))))
    n=n//10
    print(k)
    

print(k)
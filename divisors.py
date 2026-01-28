from math import sqrt

def divisor(n):
    l=[]
    r=int(sqrt(n))
    for i in range(1,r+1):
        if(n%i==0):
            l.append(i)
    l.append(n)
    return l
n=int(input())
print(divisor(n))
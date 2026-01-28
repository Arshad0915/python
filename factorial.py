def fac(n,pro):
    if n==0:
        return pro
    return fac(n-1,pro=pro*n)

n=int(input())
print(fac(n,1))
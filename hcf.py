def hcf_(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    while(n2!=0):
        div=n2
        n2=n1%div
        n1=div

    return n1
a=int(input())
b=int(input())
print(hcf_(a,b))


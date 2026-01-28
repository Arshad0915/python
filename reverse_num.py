def rev_num(n):
    a=str(n)
    return int(a[::-1])
n=int(input())
print(rev_num(n))

def rev_num_1(n):
    sign=-1 if n<0 else 1
    a=abs(n)
    rev=0
    while(a>0):
        rev=rev*10+a%10
        a//=10
    return sign*rev

a=int(input())
print(rev_num_1(a))


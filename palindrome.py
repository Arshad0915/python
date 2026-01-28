def rev_num_1(n):
    sign=-1 if n<0 else 1
    a=abs(n)
    rev=0
    while(a>0):
        rev=rev*10+a%10
        a//=10
    return sign*rev

def is_palindrome(n):
    if(n<0):
        return False
    return n==rev_num_1(n)
n=int(input())
print(is_palindrome(n))

def palin(n):
    if n<0:
        return False
    a=str(n)
    l,r=0,len(a)-1
    while(l<r):
        if a[l]!=a[r]:
            return False
        l+=1
        r-=1
    return True


a=int(input())
print(palin(a))
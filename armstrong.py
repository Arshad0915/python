def count_digi(n):
    cnt=0
    while n>0:
        n=n//10
        cnt+=1
    return cnt

def is_armstrong(n):
    original=n
    sum=0
    c=count_digi(n)
    while(n>0):
        r=n%10
        sum+=pow(r,c)
        n//=10
    return sum==original
n=int(input())
print(is_armstrong(n))

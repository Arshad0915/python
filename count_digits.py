
def count_digi(n):
    cnt=0
    while n>0:
        n=n//10
        cnt+=1
    return cnt

n=int(input())
print(count_digi(n))

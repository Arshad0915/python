def sum_1_n(n,sum):
    if n<1:
        return sum
    return sum_1_n(n-1,sum=sum+n)

n=int(input())
print(sum_1_n(n,0))
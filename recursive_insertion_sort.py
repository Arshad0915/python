def recursive_insertion_sort(nums,i,n):
    if i==n:
        return
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
    return recursive_insertion_sort(nums,i+1,n)

l=list(map(int,input().split()))
recursive_insertion_sort(l,1,len(l))
print(l)
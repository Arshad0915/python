def recursive_bubble_sort(nums,n):
    if n==1:
        return
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
    recursive_bubble_sort(nums,n-1)

l=list(map(int,input().split()))
recursive_bubble_sort(l,len(l))
print(l)
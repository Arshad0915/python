def quick_sort(nums,l,r):
    if l>=r:
        return
    pivot=nums[l]
    i=l+1
    j=r
    while i<=j:
        while i<=j and nums[i]<=pivot:
            i+=1
        while i<=j and nums[j]>pivot:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[l],nums[j]=nums[j],nums[l]
    quick_sort(nums,l,j-1)
    quick_sort(nums,j+1,r)

l=list(map(int,input().split()))
quick_sort(l,0,len(l)-1)
print(l)





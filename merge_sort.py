def merge_sort(nums,l,r):
    if l==r:
        return
    mid=(l+r)//2
    merge_sort(nums,l,mid)
    merge_sort(nums,mid+1,r)
    merge(nums,l,mid,r)

def merge(nums,l,mid,r):
    i=l
    j=mid+1
    temp=[]
    while i<=mid and j<=r:
        if nums[i]>nums[j]:
            temp.append(nums[j])
            j+=1
        elif nums[i]<nums[j]:
            temp.append(nums[i])
            i+=1
        else:
            temp.append(nums[i])
            i+=1
    while i<=mid:
        temp.append(nums[i])
        i+=1
    while j<=r:
        temp.append(nums[j])
        j+=1
    for k in range(len(temp)):
        nums[l + k] = temp[k]


l=list(map(int,input().split()))
merge_sort(l,0,len(l)-1)
print(l)


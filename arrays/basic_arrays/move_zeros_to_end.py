def move_zeros_end(nums):
    cnt=nums.count(0)
    res=[]
    for i in nums:
        if i!=0:
            res.append(i)
    res.extend([0]*cnt)
    nums[:]=res

def optimal(nums):
    k=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[k],nums[i]=nums[i],nums[k]
            k+=1

l=list(map(int,input().split()))
move_zeros_end(l)
l2=l[:]
print(l)
optimal(l2)
print(l2)

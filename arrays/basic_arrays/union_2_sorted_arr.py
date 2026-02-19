def union(nums1,nums2):
    i=0
    j=0
    res=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]>nums2[j]:
            if not res or res[-1]!=nums2[j]:
                res.append(nums2[j])
                j+=1
        elif nums1[i]<nums2[j]:
            if not res or res[-1]!=nums1[i]:
                res.append(nums1[i])
                i+=1
        else:
            if not res or res[-1]!=nums1[i]:
                res.append(nums1[i])
                i+=1
                j+=1
    while i<len(nums1):
        if res[-1]!=nums1[i]:
            res.append(nums1[i])
        i+=1
    while j<len(nums2):
        if res[-1]!=nums2[j]:
            res.append(nums2[j])
        j+=1
    return res

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
result=union(l1,l2)
print(result)
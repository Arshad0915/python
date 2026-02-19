# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
#
#
# Example 1
#
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
#
# Output: nums = [3, 4, 5, 6, 1, 2]
#
# Explanation:
#
# rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
#
# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
#
# Example 2
#
# Input: nums = [3, 4, 1, 5, 3, -5], k = 8
#
# Output: nums = [1, 5, 3, -5, 3, 4]
#
# Explanation:
#
# rotate 1 step to the left: [4, 1, 5, 3, -5, 3]
#
# rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]
#
# rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]
#
# rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]
#
# rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]
#
# rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]
#
# rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]
#
# rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]

def rotate_arr_k(nums,k):
    if len(nums)<=1:
        return
    k=k%len(nums)
    for i in range(k):
        first=nums[0]
        for j in range(1,len(nums)):
            nums[j-1]=nums[j]
        nums[-1]=first

def rotate_arr_k_optimal(nums,k):
    n=len(nums)
    if n<=1:
        return
    k=k%n
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    reverse(nums,0,n-1)

def reverse(nums,l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1

l=list(map(int,input().split()))
k=int(input())
l1=l[:]
l2=l[:]
rotate_arr_k(l1,k)
print(l1)
rotate_arr_k_optimal(l2,k)
print(l2)
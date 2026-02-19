# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
#
#
# Example 1
#
# Input : nums = [1, 2, 3, 4, 5]
#
# Output : true
#
# Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.
#
# Example 2
#
# Input : nums = [1, 2, 1, 4, 5]
#
# Output : false
#
# Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

def is_sorted(nums):
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True

def lsorted(nums):
    return nums==sorted(nums)

l=list(map(int,input().split()))
print(is_sorted(l))
print(lsorted(l))

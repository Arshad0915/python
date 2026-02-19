# Given an integer array nums, rotate the array to the left by one.
#
#
#
# Note: There is no need to return anything, just modify the given array.
#
#
# Example 1
#
# Input: nums = [1, 2, 3, 4, 5]
#
# Output: [2, 3, 4, 5, 1]
#
# Explanation:
#
# Initially, nums = [1, 2, 3, 4, 5]
#
# Rotating once to left -> nums = [2, 3, 4, 5, 1]
#
# Example 2
#
# Input: nums = [-1, 0, 3, 6]
#
# Output: [0, 3, 6, -1]
#
# Explanation:
#
# Initially, nums = [-1, 0, 3, 6]
#
# Rotating once to left -> nums = [0, 3, 6, -1]

def left_rotate_arr_1(nums):
    first=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[len(nums)-1]=first

l=list(map(int,input().split()))
left_rotate_arr_1(l)
print(l)

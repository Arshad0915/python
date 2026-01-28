# Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.
#
#
#
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.
#
#
# Example 1
#
# Input: nums = [7, 4, 1, 5, 3]
#
# Output: [1, 3, 4, 5, 7]
#
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
#
# Thus the array is sorted in non-decreasing order.
#
# Example 2
#
# Input: nums = [5, 4, 4, 1, 1]
#
# Output: [1, 1, 4, 4, 5]
#
# Explanation: 1 <= 1 <= 4 <= 4 <= 5.
#
# Thus the array is sorted in non-decreasing order.
import sys


def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        min=sys.maxsize
        min_idx=i
        for j in range(i,n):
            if nums[j]<min:
                min=nums[j]
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]
    return nums

l=list(map(int,input().split()))
res=selection_sort(l)
print(res)


# Given an array of integers nums, return the value of the largest element in the array
#
#
# Example 1
#
# Input: nums = [3, 3, 6, 1]
#
# Output: 6
#
# Explanation: The largest element in array is 6
#
# Example 2
#
# Input: nums = [3, 3, 0, 99, -40]
#
# Output: 99
#
# Explanation: The largest element in array is 99
import sys


def largest(nums):
    return max(nums)

def largest_loops(nums):
    max=-sys.maxsize-1
    for i in nums:
        if i>max:
            max=i
    return max

l=list(map(int,input().split()))
print(largest(l))
print(largest_loops(l))
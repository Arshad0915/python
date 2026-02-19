# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
#
#
# Example 1
#
# Input: nums = [8, 8, 7, 6, 5]
#
# Output: 7
#
# Explanation:
#
# The largest value in nums is 8, the second largest is 7
#
# Example 2
#
# Input: nums = [10, 10, 10, 10, 10]
#
# Output: -1
#
# Explanation:
#
# The only value in nums is 10, so there is no second largest value, thus -1 is returned
import sys


def second_largest(nums):
    if len(nums)<2:
        return None
    largest=max(nums)
    filtered= [x for x in nums if x!=largest]
    if not filtered:
        return None
    return max(filtered)

def second_largest_loops(nums):
    if len(nums)<2:
        return None
    largest=second_large=-sys.maxsize-1
    for i in nums:
        if i>largest:
            second_large=largest
            largest=i
        elif i!=largest and i>second_large:
            second_large=i
    if second_large==-sys.maxsize-1:
        return None
    return second_large




l=list(map(int,input().split()))
res=second_largest(l)
if res is None:
    print(-1)
else:
    print(res)

print(second_largest_loops(l))

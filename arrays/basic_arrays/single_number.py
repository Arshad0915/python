# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
#
#
# Example 1
#
# Input : nums = [1, 2, 2, 4, 3, 1, 4]
#
# Output : 3
#
# Explanation : The integer 3 has appeared only once.
#
# Example 2
#
# Input : nums = [5]
#
# Output : 5
#
# Explanation : The integer 5 has appeared only once.

def single_number(nums):
    xor=0
    for i in nums:
        xor^=i
    return xor

l=list(map(int,input().split()))
res=single_number(l)
print(res)
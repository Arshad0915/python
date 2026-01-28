# Given an array nums of size n which may contain duplicate elements.
#
#
#
# Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.
#
#
#
# You may return the result in any order, but each element must appear exactly once in the output.
#
#
# Example 1
#
# Input: nums = [1, 2, 2, 1, 3]
#
# Output: [[1, 2], [2, 2], [3, 1]]
#
# Explanation:
#
# - 1 appears 2 times
#
# - 2 appears 2 times
#
# - 3 appears 1 time
#
# Order of output can vary.

def freq_count(arr):
    res=[]
    for i in set(arr):
        res.append([i,arr.count(i)])
    return res
def freq_count_dict(arr):
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    return [[key,val] for key,val in d.items()]

arr=list(map(int,input().split()))
res=freq_count(arr)
res1=freq_count_dict(arr)
print(res)
print(res1)


"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and 
returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""
class Solution:
    def removeDuplicates(self, nums):
        len_arr  = len(nums)
        len_uniq = 0
        





if __name__ == "__main__":
    test = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    res = sol.threeSum(test)
    print(res)
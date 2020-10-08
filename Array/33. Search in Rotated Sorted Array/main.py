"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] 
might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -1
        left,right = 0, len(nums)-1
        while(left < right):
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            mid = (left+right)//2


        
        
        

                    
        


if __name__ == "__main__":
    test = [4,5,6,7,0,1,2]
    val  = 0
    sol = Solution()
    res = sol.search(test, val)
    print(res)
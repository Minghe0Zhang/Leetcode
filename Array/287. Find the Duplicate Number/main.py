"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums? (hash table)
Can you solve the problem using only constant, O(1) extra space? (sort the arry)
Can you solve the problem with runtime complexity less than O(n2)?
 
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        cur = 0
        for i in range(1,n):
            if nums[i] == nums[cur]:
                return nums[i]
            else:
                cur+=1
            


        
            

        
            
        
        
        
        
if __name__ == "__main__":
    nums = [1,1,2]
    sol = Solution()
    res = sol.findDuplicate(nums)
    print(res) 
    
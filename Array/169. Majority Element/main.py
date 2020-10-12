"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return None
        cur,curcnt = nums[0],1
        for i in range(1,length):
            if curcnt == 0:
                cur = nums[i]
                
            if nums[i] == cur:
                curcnt += 1
            else:
                curcnt -= 1

        if curcnt > 0:
            return cur
        else:
            return None
        

        
        
        
        
if __name__ == "__main__":
    numbers = [3,2,3]
    sol = Solution()
    res = sol.majorityElement(numbers)
    print(res)
    
"""

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
 
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=j=0
        length  = len(nums)
        max_len = 0
        while(j < length):
            if nums[j]==0:
                j +=1
                i = j
            else:
                j+=1
                max_len = max(max_len, j-i)
        return max_len
        
        
if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    sol = Solution()
    res = sol.findMaxConsecutiveOnes(nums)
    print(res) 
    
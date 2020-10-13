"""
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or 
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count 
as extra space for the purpose of space complexity analysis.)
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left = [nums[0]] * length
        right = [nums[-1]] * length
        for i in range(length-1):
            left[i+1] = left[i] * nums[i+1]
        for i in reversed(range(length-1)):
            right[i] = right[i+1] * nums[i]
        ans  = [0] * length
        for i in range(1,length-1):
            ans[i] = left[i-1]*right[i+1]
        ans[0] = right[1]
        ans[-1] = left[-2]
        return ans
        
        
        
if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    res = sol.productExceptSelf(nums)
    print(res) # [24,12,8,6]
    
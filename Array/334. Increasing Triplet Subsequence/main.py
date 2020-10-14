"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 3:
            return False

        min1_num = float('inf')
        min2_num = float('inf')

        for n in nums:
            if n < min1_num:
                min1_num = n
            elif min1_num < n and min2_num >= n:
                min2_num = n
            elif n > min2_num:
                return True

        return False

            


        
            

        
            
        
        
        
        
if __name__ == "__main__":
    nums = [5,8,0,0,0,0,7]
    sol = Solution()
    res = sol.increasingTriplet(nums)
    print(res) 
    
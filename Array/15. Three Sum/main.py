"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
 Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        len_arr = len(nums)
        a   = 0
        for a in range(len_arr -2):
            if (a>0 and nums[a]==nums[a-1]):
                continue
            left  = a + 1
            right = len_arr - 1

            while(left < right):
                if(nums[left]+nums[right]+nums[a] < 0):
                    left = left + 1
                elif(nums[left]+nums[right]+nums[a] > 0):
                    right = right - 1
                else:
                    res.append([nums[a],nums[left],nums[right]])
                    while(left<right and nums[left+1]==nums[left]):
                        left = left + 1
                    while(left<right and nums[right-1]==nums[right]):
                        right = right - 1
                    right = right - 1
                    left = left + 1
        return res




if __name__ == "__main__":
    test = [-1,0,1,2,-1,-4]
    sol = Solution()
    res = sol.threeSum(test)
    print(res)
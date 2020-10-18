"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as 
the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has 
the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_dict = {}
        for num in nums:
            if num in arr_dict:
                arr_dict[num] += 1
            else:
                arr_dict[num] = 1
        max_num, max_cnt = 0, 0
        for key in arr_dict.keys():
            if arr_dict[key] > max_cnt:
                max_cnt = arr_dict[key]
                max_num = [key]
            elif arr_dict[key] == max_cnt:
                max_num.append(key)

        ans = len(nums)
        for n in max_num:
            l, r = 0, len(nums)-1
            while(nums[l] != n):
                l+=1
            while (nums[r] != n):
                r-=1
            ans = min(r-l+1,ans)
        return ans


                
                

        
            
  
        
if __name__ == "__main__":
    nums = [1,2,2,3,1]
    sol = Solution()
    res = sol.findShortestSubArray(nums)
    print(res) 
    

    
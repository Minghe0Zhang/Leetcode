"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, 
one of the numbers in the set got duplicated to another number in the set, which results in 
repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice and then find the number that is missing. 
Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n         = len(nums)
        s         = []
        duplicate = -1
        for i in range(n):
            if nums[i] not in s:
                s.append(nums[i])
            else:
                duplicate = nums[i]
                break
        miss = duplicate - (sum(nums)-(1+n)*n//2)
        return duplicate, miss    
                    
            
  
        
if __name__ == "__main__":
    nums = [1,2,2,4]

    sol = Solution()
    res,miss = sol.findErrorNums(nums)
    print(res,miss) 
    

    
"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest 
length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element 
in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate 
element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
"""
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mask    = set()
        # n       = len(nums)
        # max_len = 0
        # for start in range(n):
        #     if start not in mask:
        #         count = 1
        #         mask.add(start)
        #         des = nums[start]
        #         while(des!=start):
        #             mask.add(des)
        #             des = nums[des]  
        #             count+=1
        #         max_len = max(max_len,count)
        # return max_len
        n       = len(nums)
        max_len = 0
        for start in range(n):
            if nums[start]!=n:
                count = 1
                des = nums[start]
                while(des!=start):
                    temp      = nums[des]
                    nums[des] = n
                    des       = temp
                    count+=1
                max_len = max(max_len,count)
                nums[start]=n
        return max_len

            
  
        
if __name__ == "__main__":
    nums = [5,4,0,3,1,6,2]

    sol = Solution()
    res = sol.arrayNesting(nums)
    print(res) 
    

    
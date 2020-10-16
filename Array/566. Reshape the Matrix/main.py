"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix 
into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers 
r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same 
row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; 
Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]):
            return nums
        res = [[0]*c for _ in range(r)]
        # print(len(res),len(res[0]))
        if len(nums)==0 or len(nums[0])==0:
            return []
        
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                idx = i*len(nums[0])+j
                res[idx//c][idx%c] = nums[i][j]
        return res
            
  
        
if __name__ == "__main__":
    nums = [[1,2],
            [3,4]]
    r = 2
    c = 4

    sol = Solution()
    res = sol.matrixReshape(nums,r,c)
    print(res) 
    

    
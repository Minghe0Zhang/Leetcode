"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
"""
import math
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        array = []
        n = len(matrix)
        for i  in range(n):
            for j in range(n):
                array.append(matrix[i][j])

        array.sort()
        return array[k-1]
        

        

            


        
            

        
            
        
        
        
        
if __name__ == "__main__":
    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
    ]
    k = 8
    sol = Solution()
    res = sol.kthSmallest(matrix, k)
    print(res) 
    
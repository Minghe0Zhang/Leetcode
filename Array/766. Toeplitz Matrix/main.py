"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m , n = len(matrix), len(matrix[0])
        cur_r = matrix[0]
        for i in range(1,m):
            if matrix[i][1:]!=cur_r[:n-1]:
                return False
            cur_r = matrix[i]
        return True

                
                

        
            
  
        
if __name__ == "__main__":
    matrix = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]
        ]
    sol = Solution()
    res = sol.isToeplitzMatrix(matrix)
    print(res) 
    

    
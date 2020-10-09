"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return
        m = len(matrix)
        n = len(matrix[0])
        is_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        print(matrix)
        print(is_col)
        for i in range(1,m):
                for j in range(1,n):
                    if matrix[i][0] == 0 or matrix[0][j]==0:
                        matrix[i][j] = 0
                        
            
        if matrix[0][0] == 0:    
            for j in range(n):
                matrix[0][j] = 0
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
        
        print(matrix)
        return


 
if __name__ == "__main__":
    test1  = [[1,1,1],[1,0,1],[1,1,1]]
    test2  = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    test3  = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    sol = Solution()
    res = sol.setZeroes(test3)
    print(res) #[[1,0,1],[0,0,0],[1,0,1]] or [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
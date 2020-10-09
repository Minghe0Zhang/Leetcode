"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix = matrix[::-1] # Use this is not in-place!!!
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # tmp = matrix[i][j]
                # matrix[i][j] = matrix[j][i]
                # matrix[j][i] = tmp
                
        print(matrix)
        

        


if __name__ == "__main__":
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol = Solution()
    sol.rotate(matrix)
    #[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def printSquare(self,matrix,offset):
        # print(matrix)
        res = []
        for i in range(offset,len(matrix[0])-offset):
            res.append(matrix[0+offset][i])
        for j in range(1+offset, len(matrix)-offset):
            res.append(matrix[j][-1-offset])
        if len(matrix)-2*offset > 1:
            for i in reversed(range(offset,len(matrix[0])-1-offset)):
                res.append(matrix[-1-offset][i])
        if len(matrix[0])-2*offset > 1:
            for j in reversed(range(1+offset,len(matrix)-1-offset)):
                res.append(matrix[j][0+offset])
        return res

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return None
        len_row = len(matrix)
        len_col = len(matrix[0])
        res     = []
        for i in range(min(len_col+1,len_row+1)//2):
            res = res + self.printSquare(matrix,offset=i)
        return res

        


if __name__ == "__main__":
    test = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    res = sol.spiralOrder(test)
    print(res)
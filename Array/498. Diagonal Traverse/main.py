"""

Given a matrix of M x N elements (M rows, N columns), 
return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m ==0:
            return []
        n = len(matrix[0])
        if n ==0:
            return []
        res = []
        reverse = False
        s = 0
        while(s <= m+n-2):
            if not reverse:
                for j in range(min(s+1,n)):
                    if s-j<=m-1:
                        res.append(matrix[s-j][j])
            else:
                for i in range(min(s+1,m)):
                    if s-i<=n-1:
                        res.append(matrix[i][s-i])

            reverse = not reverse
            s += 1
        return res
  
        
if __name__ == "__main__":
#     matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
    matrix = [[2,3]]
    sol = Solution()
    res = sol.findDiagonalOrder(matrix)
    print(res) #[1,2,4,7,5,3,6,8,9]
    

    
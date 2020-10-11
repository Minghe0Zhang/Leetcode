"""
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # if rowIndex <=2:
        #     res = [1]*rowIndex
        # res = []
        # for i in range(rowIndex):
        #     res.append(1)
        #     pre = res[:]
        #     for j in range(1,i):
        #         res[j] = pre[j]+pre[j-1]
        # return res
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in reversed(range(1,i)):
                pascal[j] += pascal[j-1]
        return pascal

        
        
        
 
if __name__ == "__main__":
    test= 3
    sol = Solution()
    res = sol.getRow(test)
    print(res)
    
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # ## Brute-Force:
        # if numRows ==0:
        #     return []
        # res = []
        # for i in range(numRows):
        #     if i==0:
        #         res.append([1])
        #         continue
        #     pre = [0] + res[i-1] + [0]
        #     # print(pre)
        #     cur = []
        #     for k in range(i+1):
        #         cur.append(pre[k]+pre[k+1])
        #     # print(cur)
        #     res.append(cur)
        #     print(res)
        # return res

        # Better
        res = []
        for i in range(numRows):
            tmp = [1]*(i+1)
            for j in range(1, i):
                tmp[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(tmp)

        return res

        
        
 
if __name__ == "__main__":
    test= 5
    sol = Solution()
    res = sol.generate(test)
    print(res)
    
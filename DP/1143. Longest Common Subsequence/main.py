class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
    
        # def dfs(text1, text2):
        #     if not text1 or not text2:
        #         return 0
        #     if text1[0] == text2[0]:
        #         return 1 + dfs(text1[1:], text2[1:])
        #     one = dfs(text1[1:], text2)
        #     two = dfs(text1, text2[1:])
        #     return max(one, two)
        # return dfs(text1, text2)
        
        def dp(text1, text2):
            A = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
            for i in range(1, len(text1) + 1):
                for j in range(1, len(text2) + 1):
                    if text1[i - 1] == text2[j - 1]:
                        A[i][j] = A[i - 1][j - 1] + 1
                    else:
                        A[i][j] = max(A[i - 1][j], A[i][j - 1])
            return A[-1][-1]
        return dp(text1, text2)
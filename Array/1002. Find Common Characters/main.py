"""
Given an array A of strings made only from lowercase letters, return a list of 
all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

"""
import collections
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return None
        ans  = list(A[0])
        for i in range(1,len(A)):
            temp       = []
            cur_string = A[i]
            for c in cur_string:
                if c in ans:
                    del ans[ans.index(c)]
                    temp.append(c)
            ans = temp
        return ans
        
        
        
if __name__ == "__main__":
    A = ["bella","label","roller"]
    sol = Solution()
    res = sol.commonChars(A)
    print(res) 
    

    
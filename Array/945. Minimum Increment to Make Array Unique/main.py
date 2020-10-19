"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

"""
import collections
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n       = len(A)
        max_a, min_a = max(A), min(A)
        count   = collections.Counter(A)
        cur_sum = sum(A)
        ans     = 0
        stack   = []
        for i in range(min_a, max_a):
            if i in count:
                stack += [i]*(count[i]-1)
            else:
                if stack:
                    ans += i-stack.pop()
        return ans + sum(range(max_a, max_a+len(stack)))
                    
        
        
        
        return move
        
        
        
if __name__ == "__main__":
    A = [3,2,1,2,1,7]
    sol = Solution()
    res = sol.minIncrementForUnique(A)
    print(res) 
    

    
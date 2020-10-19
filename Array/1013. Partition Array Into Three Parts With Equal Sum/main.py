"""
Given an array A of integers, return true if and only if we can partition the array into three
 non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j 
with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] 
== A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

"""
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        total_sum = sum(A)
        if total_sum%3!=0:
            return False
        sub_sum     = total_sum//3
        partial_sum = 0
        count       = 0
        for i in range(n):
            partial_sum += A[i]
            if partial_sum == sub_sum:
                count+=1
                partial_sum = 0
        if count >=3 and partial_sum==0:
            return True
        else:
            return False
        
        
        
        
if __name__ == "__main__":
    A = [0,2,1,-6,6,7,9,-1,2,0,1]
    sol = Solution()
    res = sol.canThreePartsEqualSum(A)
    print(res) 
    

    
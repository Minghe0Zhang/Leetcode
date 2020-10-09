"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element 
in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits)-1
        while(idx >=0 and digits[idx]==9):
            digits[idx]=0
            idx -= 1
        if(idx == -1):
            digits = [1] + digits
        else:
            digits[idx] += 1

        return digits


 
if __name__ == "__main__":
    test1  = [1,2,3]
    test2  = [8,9,9,9]
    sol = Solution()
    res = sol.plusOne(test2)
    print(res) #[[1,6],[8,10],[15,18]]
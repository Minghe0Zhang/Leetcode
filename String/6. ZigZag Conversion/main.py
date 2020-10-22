"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        string_array = ['']*numRows
        reverse      = False
        loc          = 0
        for c in s:
            if reverse:
                string_array[loc]+=c
                loc -= 1
                if loc == 0:
                    reverse = False
                    
            else:
                string_array[loc]+=c
                loc += 1
                if loc==numRows-1:
                    reverse = True
        ans = ''
        for i in range(numRows):
            ans = ans + string_array[i]
        return ans

if __name__ == "__main__":
    s = "AB"
    numRows = 1
    sol = Solution()
    res = sol.convert(s, numRows)
    print(res)
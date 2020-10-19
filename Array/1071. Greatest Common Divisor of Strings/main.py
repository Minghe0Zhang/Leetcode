"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  
(t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""

"""
from math import gcd
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if ( str1 + str2 ) != ( str2 + str1 ):
		
            # if str1 and str2 has no common factor, then reject
			
            return ''
			
        elif str1 == str2:
		
            # if str1 and str2 are perfect match, then we find greatest common divisor of strings
			
            return str1
			
        else:
		
            # if str1 =\= str2, then solve it by recursive with length_by_gcd
			
            length_by_gcd = gcd( len(str1), len(str2) )
            return self.gcdOfStrings( str1[:length_by_gcd], str2[:length_by_gcd] )
        
        
        
        
if __name__ == "__main__":
    str1 = "LEET" 
    str2 = "CODE"
    sol = Solution()
    res = sol.gcdOfStrings(str1, str2)
    print(res) 
    

    
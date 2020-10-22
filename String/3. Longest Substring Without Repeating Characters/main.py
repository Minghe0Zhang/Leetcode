"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

"""
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict  = collections.defaultdict()
        n       = len(s)
        max_len = 0
        start   = 0
        for i in range(n):
            if s[i] not in s_dict:
                s_dict[s[i]] = i
            else:
                if start <= s_dict[s[i]]:
                    start = s_dict[s[i]]+1
                s_dict[s[i]] = i
            max_len = max(max_len, i-start+1)

        return max_len



if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)
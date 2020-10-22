"""
输入
    5
    picture
    turepic
    icturep
    word
    ordw

输出
    2
"""

class Solution:
    def loopword(self, letterlist):
        
            




if __name__ == "__main__":
    n = int(sys.stdin.readline())
    letter_list = []
    for i in range(0, n):
        letter_list.append(str(sys.stdin.readline()).replace('\n', ''))
    sol = Solution()
    ans = sol.loopword(letter_list)
    print(ans)
        
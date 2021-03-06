"""
10-7-2020


11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints 
of the line i is at (i, ai) and (i, 0). Find two lines, which, 
together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height):
        len_arr = len(height)
        right,left = len_arr-1,0
        res  = 0
        while(left<right):
            res = max(res, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return res
            




if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    ans = sol.maxArea(height)
    print(ans)
        
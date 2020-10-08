"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.


"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_height = 0
        max_index  = -1
        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_index  = i
        # check if it is valid or not
        if max_index == -1:
            return 0
        
        area = 0

        # Left traverse
        sec_max     = height[0]
        for i in range(max_index):
            if height[i] > sec_max:
                sec_max  = height[i]
            else:
                area = area + (sec_max - height[i])


        sec_max     = height[-1]
        for j in reversed(range(max_index+1, len(height)-1)):
            if height[j] > sec_max:
                sec_max = height[j]
            else:
                area = area + (sec_max - height[j])
        return area



class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length == 0:
            return 0

        stack = []
        # 第一个元素入栈
        stack.append(0)
        ans = 0
        for i in range(1, length):
            # 栈顶元素
            top = stack[-1]
            h = height[i]
            # 循环 pop
            while len(stack) != 0 and height[stack[-1]] < h:
                # 弹出栈顶元素
                tmp = stack.pop()
                # 存在墙才计算积水
                if len(stack) == 0:
                    break
                # 计算左右两侧高度 min
                diff = min(height[stack[-1]], h)
                distance = i - stack[-1] - 1
                ans += distance * (diff - height[tmp])

            stack.append(i)

        return ans



    

        


if __name__ == "__main__":
    test = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution2()
    res = sol.trap(test)
    print(res)
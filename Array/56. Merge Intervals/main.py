"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0 or len(intervals) ==1:
            return intervals
        intervals = sorted(intervals, key=lambda a:a[0])
        res   = []
        flag  = False # flag to check if merge is sucessful in the previous turn
        for i in range(len(intervals)-1):
            if flag:
                if(res[-1][1] >= intervals[i+1][0]):
                    res[-1][1] = max(intervals[i+1][1], res[-1][1])
                else:
                    # res.append(intervals[i+1])
                    flag = False
            else:
                if(intervals[i][1]>= intervals[i+1][0]):
                    res.append([intervals[i][0],max(intervals[i][1],intervals[i+1][1])])
                    flag = True
                else:
                    res.append(intervals[i])
        if not flag:
            res.append(intervals[-1])
        return res


        # length = len(intervals)

        # if length <= 1:
        #     return intervals

        # intervals.sort()
        # res = list()

        # for i in range(length - 1):
        #     left = intervals[i]
        #     right = intervals[i + 1]

        #     if left[1] >= right[0]:
        #         # 区间可合并
        #         if left[1] < right[1]:
        #             new_list = [left[0], right[1]]
        #         else:
        #             new_list = [left[0], left[1]]
        #         intervals[i + 1] = new_list
        #     else:
        #         res.append(left)

        # res.append(intervals[-1])
        # return res
        

        


if __name__ == "__main__":
    test = [[1,3],[8,10],[2,6],[15,18]]
    test2 = [[1,4],[4,5]]
    sol = Solution()
    res = sol.merge(test2)
    print(res) #[[1,6],[8,10],[15,18]]
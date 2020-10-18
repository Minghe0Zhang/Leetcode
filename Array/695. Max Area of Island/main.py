"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution(object):
    def dfs(self, grid, r,c):
        m, n = len(grid), len(grid[0])
        if grid[r][c]==0:
            return 0
        else:
            grid[r][c]=0
            cur_area  =1
            if r<m-1:
                cur_area += self.dfs(grid, r+1,c)
            if r>0:
                cur_area += self.dfs(grid, r-1,c)
            if c<n-1:
                cur_area += self.dfs(grid, r,c+1)
            if c>0:
                cur_area += self.dfs(grid, r,c-1)
            return cur_area
            
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        max_area = 0
        if m==0 or n==0:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    cur_area = self.dfs(grid, i,j)
                    max_area = max(max_area, cur_area)
        return max_area
        
        
            
  
        
if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution()
    res = sol.maxAreaOfIsland(grid)
    print(res) 
    

    
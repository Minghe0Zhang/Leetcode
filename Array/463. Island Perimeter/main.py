"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and 
grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around 
the island. One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.

 
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i==0 or grid[i-1][j]==0:
                        res += 1
                    if i==n-1 or grid[i+1][j]==0:
                        res += 1
                    if j==0 or grid[i][j-1]==0:
                        res +=1
                    if j==m-1 or grid[i][j+1]==0:
                        res += 1
        return res

        
if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    sol = Solution()
    res = sol.islandPerimeter(grid)
    print(res) 
    
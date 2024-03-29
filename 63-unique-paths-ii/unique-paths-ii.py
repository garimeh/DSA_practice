class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def help(i,j):
            if i == 0 and j == 0 and grid[i][j] != 1:
                return 1
            if i<0 or j<0: return 0
            if i>= 0 and j >= 0 and grid[i][j] == 1: 
                dp[i][j] = 0
                return 0
            if dp[i][j] != -1: return dp[i][j]
            up = help(i-1,j)
            left = help(i,j-1)
            dp[i][j] = up+left
            return up+left
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        return help(m-1,n-1)
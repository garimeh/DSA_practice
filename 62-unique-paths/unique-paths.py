class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*n
        for i in range(m):
            temp = [0]*n
            for j in range(n):
                if i == 0 and j == 0: 
                    temp[j] = 1 
                else: 
                    up = 0
                    left = 0
                    up = dp[j] 
                    if j>0: left = temp[j-1]
                    temp[j] = up+left
            dp = temp
        return dp[n-1]
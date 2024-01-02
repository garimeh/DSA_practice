class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]

        def help(ind, rem):
            if ind == n:
                return 1 if rem == 0 else 0
            if rem < 0:
                return 0
            if dp[ind][rem] != -1:
                return dp[ind][rem]
            
            ans = 0
            for i in range(1, k + 1): 
                ans = (ans + help(ind + 1, rem - i)) % mod

            dp[ind][rem] = ans
            return dp[ind][rem]

        return help(0, target)

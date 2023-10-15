class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1e9 + 7
        memo = {}
        @cache
        def help(i, s):
            if i == 0 and s == 0:
                return 1
            if s == 0 :
                return 0
            if (i,s) in memo:
                return memo[(i,s)]
            left, right = 0,0
            if i-1>=0: 
                left = help(i-1, s-1)
            if i+1<arrLen: 
                right = help(i+1, s-1)
            stay = help(i, s-1)
            memo[(i,s)] = (left + right + stay)%MOD
            return (left + right + stay) % MOD
        return int(help(0, steps))
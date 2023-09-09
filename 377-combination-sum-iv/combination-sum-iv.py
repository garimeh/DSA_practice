class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [-1]*(target+1)
        def recur(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if dp[t] != -1:
                return dp[t]
            comb = 0
            for num in nums:
                comb += recur(t - num)
            dp[t] = comb
            return comb
        return recur(target)
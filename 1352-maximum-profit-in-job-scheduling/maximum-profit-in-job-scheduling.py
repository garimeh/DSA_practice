class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time = sorted(zip(endTime, startTime, profit))
        dp = [0]*(len(profit)+1)
        for i, (curend, curst, prof) in enumerate(time):
            ind = bisect_right(time, curst, hi = i, key = lambda x: x[0])
            dp[i+1] = max(dp[i], dp[ind] + prof)
        return dp[len(profit)]
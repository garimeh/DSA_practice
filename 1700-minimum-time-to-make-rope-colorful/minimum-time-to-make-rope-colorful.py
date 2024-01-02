class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        prev_color = colors[0]
        cur_sum = neededTime[0]
        max_time = neededTime[0]

        for i in range(1, n):
            if colors[i] == prev_color:
                cur_sum += neededTime[i]
                max_time = max(max_time, neededTime[i])
            else:
                ans += cur_sum - max_time
                prev_color = colors[i]
                cur_sum = neededTime[i]
                max_time = neededTime[i]

        ans += cur_sum - max_time  

        return ans

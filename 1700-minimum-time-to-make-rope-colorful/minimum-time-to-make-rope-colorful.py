class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        l = 0
        for r in range(1, n):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    ans += neededTime[l]
                    l = r
                else:
                    ans += neededTime[r]
            else:
                l = r
        return ans

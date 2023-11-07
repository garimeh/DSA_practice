class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = 0
        n = len(dist)
        time = [0]*n

        for i in range(n):
            time[i] = dist[i]/speed[i]
        
        time.sort()

        for i in range(n):
            if time[i] <= i:
                break
            ans += 1
        return ans
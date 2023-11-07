class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = 0
        n = len(dist)
        time = [0]*n

        for i in range(n):
            time[i] = dist[i]/speed[i]
        
        heapq.heapify(time)

        while time:
            if heapq.heappop(time) <= ans:
                break
            ans += 1
        return ans
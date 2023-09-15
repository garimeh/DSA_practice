import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        mincst = 0
        vis = [0]*n
        pq = [(0,0)]

        def dist(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        while pq:
            c,u = heapq.heappop(pq)
            if vis[u]:
                continue
            vis[u] = 1
            mincst += c
            for v in range(n):
                if not vis[v]:
                    d = dist(points[u], points[v])
                    heapq.heappush(pq,(d,v))
        return mincst
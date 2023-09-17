import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        dist = [[float("inf") for _ in range(c)] for _ in range(r)]
        dirx = [(1,0), (0,1), (-1,0), (0,-1)]
        dist[0][0] = 0
        heap = [(0,0,0)]

        while heap:
            ef, x,y = heappop(heap)
            if x==r-1 and y == c-1:
                return ef
            for dx , dy in dirx:
                nx , ny = x+dx, y+dy

                if 0<=nx<r and 0<=ny<c :
                    nef = max(ef, abs(heights[x][y] - heights[nx][ny]))

                    if nef < dist[nx][ny]:
                        dist[nx][ny] = nef
                        heappush(heap,(nef, nx,ny))
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Manhattan distance between two points
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        minCost = [float('inf')] * n
        visited = [False] * n
        minCost[0] = 0
        
        total_cost = 0
        for _ in range(n):
            u = self.getMinCostVertex(minCost, visited)
            visited[u] = True
            total_cost += minCost[u]
            
            for v in range(n):
                if not visited[v] and manhattan(points[u], points[v]) < minCost[v]:
                    minCost[v] = manhattan(points[u], points[v])
                    
        return total_cost

    def getMinCostVertex(self, cost, visited):
        minVal = float('inf')
        minIndex = -1
        
        for v in range(len(cost)):
            if not visited[v] and cost[v] < minVal:
                minVal = cost[v]
                minIndex = v
                
        return minIndex
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[] for _ in range(n)]
        for fro, to, cost in edges:
            self.adj[fro].append((to, cost))

    def addEdge(self, edge: List[int]) -> None:
        fro, to, co = edge
        self.adj[fro].append((to,co))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adj)
        pq = [(0, node1)]
        cfn = [inf]*n
        cfn[node1] = 0

        while pq:
            curcost, curnode = heappop(pq)
            if curcost > cfn[curnode]:
                continue
            if curnode == node2:
                return curcost
            for ne, co in self.adj[curnode]:
                newc = curcost + co
                if newc < cfn[ne]:
                    cfn[ne] = newc
                    heappush(pq, (newc, ne))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
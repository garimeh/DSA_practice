import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            heappush(heap, (sum(row), i))  
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
            
        return ans                 
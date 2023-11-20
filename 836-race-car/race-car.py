import heapq
class Solution:
    def racecar(self, t: int) -> int:
        q = [(0,0,1)]
        vis = set()
        while q:
            moves, pos, sp = heappop(q)

            if pos == t:
                return moves

            if (pos, sp) in vis:
                continue
            
            vis.add((pos, sp))
            heapq.heappush(q, (moves+1, pos + sp, sp*2))

            if (pos + sp > t and sp > 0) or (pos + sp < t and sp < 0):
                sp = -1 if sp > 0 else 1
                heapq.heappush(q, (moves + 1, pos, sp)) 

        return -1 
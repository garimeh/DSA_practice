from collections import defaultdict
class Solution:
    def restoreArray(self, adj: List[List[int]]) -> List[int]:
        pair = defaultdict(list)
        for p,q in adj:
            pair[p].append(q)
            pair[q].append(p)

        ans = []
        s = float('-inf')
        for e in pair:
            if len(pair[e]) == 1:
                s = e
                break
        
        ans.append(s)
        seen = set()

        for i in range(1,len(adj) + 1):
            ne = pair[s][0] if pair[s][0] not in seen else pair[s][1]
            ans.append(ne)
            seen.add(s)
            s = ne

        return ans

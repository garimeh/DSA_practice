from collections import defaultdict

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        dst = [0] * len(garbage)
        for i in range(len(travel)):
            dst[i + 1] = dst[i] + travel[i]
        
        mp = defaultdict(int)
        m, p, g = 0, 0, 0

        for i in range(len(garbage)):
            for c in garbage[i]:
                mp[c] = i
                if c == "M":
                    m += 1
                elif c == "P":
                    p += 1
                else:
                    g += 1

        ans = 0
        for c in ["M", "P", "G"]:
            if c in mp: 
                ans += dst[mp[c]]
                if c == "M":
                    ans += m
                elif c == "P":
                    ans += p
                else:
                    ans += g
        return ans

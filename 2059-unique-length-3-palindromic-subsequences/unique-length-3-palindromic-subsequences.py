class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ind = {}
        for i in range(len(s)):
            if s[i] not in ind:
                ind[s[i]] = ind.get(s[i], [-1, -1])
                ind[s[i]][0] = i
            else:
                ind[s[i]][1] = i
        
        ans = 0

        for st, end in ind.values():
            seen = set()
            for i in range(st+1,end):
                seen.add(s[i])
            ans += len(seen)
            
        return ans
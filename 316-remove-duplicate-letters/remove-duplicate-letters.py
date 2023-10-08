class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        res = []
        vis = set()
        for c in s:
            count[c] -=1
            if c in vis:
                continue
            while res and c < res[-1] and count[res[-1]] >0:
                vis.remove(res.pop())
            vis.add(c)
            res.append(c)
        return ''.join(res)
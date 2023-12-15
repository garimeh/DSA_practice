class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        for i in range(len(paths)):
            outgoing.add(paths[i][0])

        for a, b in paths:
            if b not in outgoing:
                return b
        return ""
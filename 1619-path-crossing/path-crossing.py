class Solution:
    def isPathCrossing(self, path: str) -> bool:
        map = {'N': (0,1), 'E': (1,0), 'S': (0, -1), 'W': (-1,0)}
        vis = set()
        vis.add((0,0))
        x, y = 0, 0
        for c in path:
            dx, dy = map[c]
            x += dx 
            y += dy
            if (x,y) in vis:
                return True
            vis.add((x,y))
        return False
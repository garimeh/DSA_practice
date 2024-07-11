class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dirx = True
        i = 1
        while time: 
            time -= 1
            if dirx:
                i += 1
                if i == n : 
                    dirx = not dirx
                    continue
            if not dirx:
                i -= 1
                if i == 1:
                    dirx = not dirx
                    continue
        return i
                 
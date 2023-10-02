class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0,0
        l = 0
        cnt = 0
        for r in range(len(colors)):
            if colors[l] != colors[r]:
                l = r
                cnt = 0
            if colors[l] == colors[r]:
                cnt += 1
            if cnt >= 3:
                if colors[r] == 'A':
                    a+=1
                if colors[r] == 'B':
                    b +=1 
        return a>b
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRow = [0]*m
        onescol = [0]*n
        zerosRow = [0]*m
        zeroscol = [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onescol[j] += 1 

        diff = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = 2*onesRow[i] + 2*onescol[j] - m - n

        return diff
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        ans = [[-1]*n for _ in range(m)]
        r = 0
        c = [0]*n
        for i in range(m):
            for j in range(n):
                ans[i][j] = min(rowSum[i] - r, colSum[j] - c[j])
                r += ans[i][j]
                c[j] += ans[i][j]
            r = 0
        return ans
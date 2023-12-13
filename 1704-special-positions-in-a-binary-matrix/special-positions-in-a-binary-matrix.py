class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowcnt = [0]*m
        colcnt = [0]*n

        for row in range(m):
            for col in range(n):
                if mat[row][col]==1:
                    rowcnt[row] += 1
                    colcnt[col] += 1
        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if rowcnt[row] == 1 and colcnt[col] == 1:
                        ans += 1
        return ans
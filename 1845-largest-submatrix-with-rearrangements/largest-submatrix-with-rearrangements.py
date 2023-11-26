class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] != 0 and row > 0:
                    mat[row][col] += mat[row-1][col]

            currow = sorted(mat[row], reverse=True)

            for i in range(n):
                ans = max(ans, currow[i]*(i+1))

        return ans
class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
        prevrow = [0]*n
        for row in range(m):
            currow = mat[row]
            for col in range(n):
                if currow[col] != 0:
                    currow[col] += prevrow[col]

            srow = sorted(mat[row], reverse=True)

            for i in range(n):
                ans = max(ans, srow[i]*(i+1))
                
            prevrow = currow

        return ans
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ones = set()
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue

                good = True
                for r in range(len(mat)):
                    if r != i and mat[r][j] == 1:
                        good = False
                        break
                for c in range(len(mat[0])):
                    if c != j and mat[i][c] == 1:
                        good = False
                        break
                if good:
                    ans += 1
        return ans
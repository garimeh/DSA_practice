class Solution:
    def getRow(self, r: int) -> List[int]:
        def ncr(n,r):
            res = 1
            for i in range(r):
                res = res*(n-i)
                res = res/(i+1)
            return int(res)

        ans = []
        for i in range(r+1):
            ans.append(ncr(r,i))
        return ans
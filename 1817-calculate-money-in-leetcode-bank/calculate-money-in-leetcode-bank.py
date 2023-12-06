class Solution:
    def totalMoney(self, n: int) -> int:
        k = n//7
        f = 28
        l = 28 + (k-1)*7
        asum = k*(f+l)//2

        mon = 1 + k
        fin = 0
        for d in range(n%7):
            fin += mon + d
        
        return asum + fin
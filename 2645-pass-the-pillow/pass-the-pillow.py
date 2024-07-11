class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full = time//(n-1)
        return time%(n-1) + 1 if full%2 == 0 else (n - time%(n-1))
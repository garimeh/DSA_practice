class Solution:
    def getRow(self, r: int) -> List[int]:
        res = [1]
        prev = 1
        for k in range(1, r + 1):
            next_val = prev * (r - k + 1) // k
            res.append(next_val)
            prev = next_val
        return res
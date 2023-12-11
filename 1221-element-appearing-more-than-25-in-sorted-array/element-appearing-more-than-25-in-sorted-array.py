from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = Counter(arr)
        n = len(arr)
        for num, f in freq.items():
            if f > n//4:
                return num
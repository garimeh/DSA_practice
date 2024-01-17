class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        freq = Counter(arr)
        for k, v in freq.items():
            if v in seen:
                return False
            seen.add(v)
        return True
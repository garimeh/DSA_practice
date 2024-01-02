class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        ans = []
        while any(freq.values()):
            cur = []
            for k in freq.keys():
                if freq[k] > 0:
                    cur.append(k)
                    freq[k] -= 1
            ans.append(cur)
        return ans
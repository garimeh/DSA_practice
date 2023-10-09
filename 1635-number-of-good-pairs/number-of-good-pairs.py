class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        cnt = Counter(nums)
        for c,f in cnt.items():
            res += f*(f-1)//2
        return res
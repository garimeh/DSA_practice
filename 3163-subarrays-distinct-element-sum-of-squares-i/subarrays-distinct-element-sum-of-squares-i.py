class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            fmap = set()
            cnt = 0
            for j in range(i,n):
                if nums[j] not in fmap:
                    cnt+= 1
                    fmap.add(nums[j])
                ans += cnt*cnt
        return ans
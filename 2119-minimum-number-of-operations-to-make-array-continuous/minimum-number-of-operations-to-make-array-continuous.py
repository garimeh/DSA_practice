class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        minop = float('inf')
        r = 0
        for l in range(n):
            while r < len(nums) and nums[r] < nums[l] + n:
                r += 1
            op = r - l
            minop = min(minop, n - op)
        return minop
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        prev, prev2, cur = nums[0], -1, nums[1]
        for i in range(1, n):
            take = nums[i]
            if i > 1: take += prev2
            notake = prev
            cur = max(take, notake)
            prev2 = prev
            prev = cur
        return cur
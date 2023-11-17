class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = float("-inf")

        while l < r:
            cursum = nums[l] + nums[r]
            ans = max(ans, cursum)
            l += 1
            r -= 1
            
        return ans
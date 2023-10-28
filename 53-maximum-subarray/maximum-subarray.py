class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = nums[0]
        curs = 0

        for n in nums:
            if curs < 0:
                curs = 0
            curs += n
            maxs = max(curs,maxs)
        return maxs
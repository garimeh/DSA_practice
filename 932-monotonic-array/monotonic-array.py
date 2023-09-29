class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        d = sorted(nums,reverse=True)
        a = sorted(nums)
        return (nums == a) or (nums == d)
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        def prod_diff(a,b,c,d):
            return (a*b) - (c*d)
        
        nums.sort()
        return prod_diff(nums[-1], nums[-2], nums[0], nums[1])
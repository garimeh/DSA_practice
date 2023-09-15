class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        one = 0
        for i in nums:
            one += i
        two = len(nums)*(len(nums)+1)//2
        return two-one
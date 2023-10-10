class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        i = 0
        for k in [0,1,2]:
            v = cnt[k]
            while v > 0 and i < len(nums):
                nums[i] = k 
                v -= 1
                i += 1
class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        left = self.bs(nums, t,True)
        right = self.bs(nums, t, False)
        return [left, right]

    def bs(self, nums, t, lb):
        l = 0
        r = len(nums) - 1
        i = -1
        while l<=r:
            m = (l+r)//2
            if nums[m] <t:
                l = m+1
            elif nums[m] > t:
                r = m - 1
            else:
                i = m
                if lb:
                    r = m -1 
                else:
                    l = m+1
        return i
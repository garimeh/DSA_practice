class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<2:
            return True
        dirx = 0
        for i in range(1, len(nums)):
            if nums[i]> nums[i-1]:
                if dirx == 0:
                    dirx = 1
                elif dirx == -1:
                    return False
            elif nums[i]<nums[i-1]:
                if dirx == 0:
                    dirx = -1
                elif dirx == 1:
                    return False
        return True
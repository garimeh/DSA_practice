class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = []
        while l <= r:
            if nums[l] == t and nums[r] == t:
                ans.append(l)
                ans.append(r)
                break
            if nums[l] != t:
                l += 1
            if nums[r] != t:
                r-=1
        return ans if ans else [-1,-1]
            
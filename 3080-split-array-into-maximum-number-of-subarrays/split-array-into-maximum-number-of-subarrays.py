class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        mind = reduce(and_, nums)
        if mind >0:
            return 1
        cnt , mask = 0, 2**32 - 1
        for n in nums:
            mask &= n
            if mask == 0:
                cnt +=1 
                mask = 2**32-1
        return cnt
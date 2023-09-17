from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        for f in freq.values():
            if f>1:
                return True
        return False
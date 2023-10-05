from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        n = len(nums)//3
        for el, f in d.items():
            if f > n:
                ans.append(el)
        return ans
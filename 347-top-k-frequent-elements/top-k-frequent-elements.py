from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for i in range(len(nums)):
            ans[nums[i]] += 1
        a = []
        ans = sorted(ans, key = ans.get, reverse = True)
        return ans[:k]
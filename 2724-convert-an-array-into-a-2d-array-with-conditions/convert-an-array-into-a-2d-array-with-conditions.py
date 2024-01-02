class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0]*(len(nums)+1)
        ans = []
        for n in nums:
            if freq[n] >= len(ans):
                ans.append([])
            if ans:
                ans[freq[n]].append(n)
            freq[n] += 1
        return ans
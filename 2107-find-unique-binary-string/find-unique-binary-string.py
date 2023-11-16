class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ""
        for i in range(n):
            cur = nums[i][i]
            if cur == "1":
                ans += "0"
            else:
                ans += "1"
        return ans if ans not in nums else ""
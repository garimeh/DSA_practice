from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def rev(x):
            ans = 0
            i = 0
            while x:
                ans = ans*10 + (x%10)
                x = x//10
            return ans
        
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))
        
        ans = 0
        f = defaultdict(int)
        for num in arr:
            ans = (ans + f[num])%MOD
            f[num] += 1
        return ans
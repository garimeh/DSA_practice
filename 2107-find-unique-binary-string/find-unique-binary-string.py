class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ing = set()
        for num in nums:
            ing.add(int(num, 2))
        
        n = len(nums)

        for num in range(n+1):
            if num not in ing:
                ans = bin(num)[2:]
                return "0"*(n-len(ans)) + ans

        return ""
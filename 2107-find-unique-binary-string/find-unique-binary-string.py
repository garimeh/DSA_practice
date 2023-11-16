class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ing = set()
        for num in nums:
            ing.add(int(num, 2))
        
        n = len(nums)
        ans = 0

        while ans in ing:
            ans = random.randrange(0,2**n)
        
        s = bin(ans)[2:]
        return "0"*(n-len(s)) + s
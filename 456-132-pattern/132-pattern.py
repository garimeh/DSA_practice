class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # n = len(nums)
        stack = []
        cmin = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1] and n < stack[-1][0]:
                return True
            stack.append([n, cmin])
            cmin = min(cmin, n)
        return False
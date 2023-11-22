from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diag = row + col
                groups[diag].append(nums[row][col])

        ans = []
        cur = 0

        while cur in groups:
            ans.extend(groups[cur])
            cur += 1

        return ans
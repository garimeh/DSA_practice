from sortedcontainers import SortedSet

class Solution:
    def findIndices(self, nums, indexDifference, valueDifference):
        n = len(nums)
        S = SortedSet()
        
        for i in range(n):
            if i >= indexDifference:
                x = i - indexDifference
                y = nums[x]
                S.add((y, x))

            it = S.bisect_left((nums[i] + valueDifference, 0))
            if it != len(S):
                return [S[it][1], i]
            
            it = S.bisect_left((nums[i] - valueDifference + 1, 0))
            if it != 0:
                return [S[it - 1][1], i]
        
        return [-1, -1]

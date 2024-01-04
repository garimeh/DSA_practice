from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        operations = 0
        for freq in count.values():
            if freq < 2: 
                return -1
            if freq % 3 == 0:
                operations += freq // 3
            elif freq % 3 == 1:
                if freq < 4: 
                    return -1
                operations += (freq - 4) // 3 + 2
            else:  
                operations += (freq - 2) // 3 + 1
            
        return operations
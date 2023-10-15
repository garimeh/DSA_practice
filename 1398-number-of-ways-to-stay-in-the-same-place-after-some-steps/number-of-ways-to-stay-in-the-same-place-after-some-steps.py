class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = int(1e9 + 7)
        # The farthest index we can reach is min(steps//2, arrLen-1)
        max_index = min(steps//2, arrLen-1)
        
        # Initialize memo with default values
        memo = {}
        for i in range(max_index + 1):
            for s in range(steps + 1):
                memo[(i, s)] = 0
        
        # Base case: when no steps are remaining and at index 0
        memo[(0, 0)] = 1
        
        for s in range(1, steps + 1):
            for i in range(0, max_index + 1):
                # Stay
                memo[(i, s)] = memo[(i, s-1)]
                
                # Move left
                if i-1 >= 0:
                    memo[(i, s)] += memo[(i-1, s-1)]
                
                # Move right
                if i+1 <= max_index:
                    memo[(i, s)] += memo[(i+1, s-1)]
                
                memo[(i, s)] %= MOD
    
        return memo[(0, steps)]
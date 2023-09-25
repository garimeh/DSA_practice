class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = defaultdict(int)
        t_count = defaultdict(int)
    
        for char in s:
            s_count[char] += 1
    
        for char in t:
            t_count[char] += 1
        
        for key, value in t_count.items():
            if s_count[key] != value:
                return key
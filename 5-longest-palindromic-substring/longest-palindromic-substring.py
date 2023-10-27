class Solution:
    def longestPalindrome(self, s: str) -> str:
        def help(i, j):
            l = i
            r = j-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True
        
        for l in range(len(s), 0, -1):
            for st in range(len(s)-l + 1):
                if help(st, st+l):
                    return s[st:st+l]
        return ""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def help(s,t,m,n):
            if m == 0:
                return True
            if n == 0:
                return False
            if s[m-1] == t[n-1]:
                return help(s,t,m-1,n-1)
            return help(s,t,m,n-1)
        if help(s,t,len(s), len(t)):
            return True
        return False
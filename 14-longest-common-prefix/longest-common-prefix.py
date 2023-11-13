class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0 :
            return ""
        ans = strs[0]
        i = 0
        j = 0
        for k in range(1,len(strs)):
            t = ""
            while i < len(ans) and j < len(strs[k]) and ans[i] == strs[k][j]:
                t += ans[i]
                i += 1
                j += 1
            i = 0
            j = 0
            ans = t

        return ans
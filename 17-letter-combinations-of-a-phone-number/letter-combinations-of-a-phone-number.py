class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':['a','b','c'], '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        ans = []
        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                ans.append(curstr)
                return
            for c in dic[digits[i]]:
                backtrack(i+1, curstr + c)
        if digits:
            backtrack(0, "")
        return ans
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if x > y:
            top = "ab"
            tscore = x
            bot = "ba"
            bscore = y
        else :
            top = "ba"
            tscore = y
            bot = "ab"
            bscore = x
        stack = []
        for char in s:
            if char == top[1] and stack and stack[-1] == top[0]:
                res += tscore
                stack.pop()
            else:
                stack.append(char)
        
        nstack = []
        for char in stack:
            if char == bot[1] and nstack and nstack[-1] == bot[0]:
                res += bscore
                nstack.pop()
            else:
                nstack.append(char)
        return res
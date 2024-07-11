class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curstring = ""
        for char in s:
            if char == '(':
                stack.append(curstring)
                curstring = ""
            elif char == ')':
                curstring = curstring[::-1]
                curstring = stack.pop() + curstring
            else:
                curstring += char
                
        return curstring
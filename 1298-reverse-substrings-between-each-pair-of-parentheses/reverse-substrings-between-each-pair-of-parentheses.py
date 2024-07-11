class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = []
        for i in s:
            if i != ')':
                ans.append(i)
            else:
                z = ''
                while True:
                    x = ans.pop()
                    if x == '(':
                        break
                    z += x
                for j in z:
                    ans.append(j)
        return ''.join(ans)
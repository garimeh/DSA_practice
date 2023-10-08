class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l = {c:idx for idx,c in enumerate(s)}
        seen = set()
        stack = []
        for ind,c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and ind < l[stack[-1]]:
                    seen.discard(stack.pop())
                stack.append(c)
                seen.add(c)
        return ''.join(stack)
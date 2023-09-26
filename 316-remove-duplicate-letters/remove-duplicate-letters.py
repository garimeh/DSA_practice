class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {char: index for index, char in enumerate(s)}

        for index, char in enumerate(s):
            if char not in seen:
                # Check if the current char is smaller than the last char in stack and
                # the last occurrence of the last char in stack is greater than the current index
                while stack and char < stack[-1] and index < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)

        return ''.join(stack)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Initialize stack with -1

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Pop the last index
                if not stack:
                    stack.append(i)  # If stack is empty, push current index
                else:
                    # Calculate the length of current valid substring
                    max_len = max(max_len, i - stack[-1])
    
        return max_len

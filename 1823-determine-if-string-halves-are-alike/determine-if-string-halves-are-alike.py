class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(1 for c in s[: len(s) // 2] if c.lower() in "aeiou") == sum(
            1 for c in s[len(s) // 2 :] if c.lower() in "aeiou"
        )
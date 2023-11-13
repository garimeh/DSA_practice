class Solution:
    def sortVowels(self, s: str) -> str:
        v = []
        q = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I','O', 'U']
        t = ""
        for c in s:
            if c in q:
                v.append(ord(c))

        v.sort()

        for i in range(len(s)):
            if s[i] in q:
                t += chr(v[0])
                v.pop(0)
            else:
                t += s[i]
        return t
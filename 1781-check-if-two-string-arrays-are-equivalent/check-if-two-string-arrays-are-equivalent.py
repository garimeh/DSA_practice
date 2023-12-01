class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1, w2 = 0,0
        s1, s2 = 0,0

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][s1] != word2[w2][s2]:
                return False
            s1 += 1
            s2 += 1
            if s1 == len(word1[w1]):
                w1 += 1
                s1 = 0

            if s2 == len(word2[w2]):
                w2 += 1
                s2 = 0
        return w1 == len(word1) and w2 == len(word2)
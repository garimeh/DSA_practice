from collections import Counter, defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charfreq = Counter(chars)
        ans = 0
        for word in words:
            wordcnt = Counter(word)
            
            good = True

            for c, fr in wordcnt.items():
                if charfreq[c] < fr:
                    good = False
                    break
            
            if good:
                ans += len(word)

        return ans
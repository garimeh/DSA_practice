class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:        
        chars1 = set(word1)
        chars2 = set(word2)
        
        word1CharOccurrences = [word1.count(chr) for chr in chars1]
        word2CharOccurrences = [word2.count(chr) for chr in chars2]
    
        return len(word1) == len(word2) and chars1 == chars2 and sorted(word1CharOccurrences) == sorted(word2CharOccurrences)
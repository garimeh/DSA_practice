class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def compare(a):
            return (bin(a)[2:].count("1"), a) 

        arr.sort(key = compare)
        return arr
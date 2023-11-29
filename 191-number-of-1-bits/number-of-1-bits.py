class Solution:
    def hammingWeight(self, n: int) -> int:
        st = bin(n)[2:]
        return st.count('1')
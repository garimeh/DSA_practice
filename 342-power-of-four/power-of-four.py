class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0: return False

        lg4 = math.log(n)/math.log(4)

        return lg4 == int(lg4)
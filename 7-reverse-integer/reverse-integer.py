class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        n = 0
        while x:
            p = int(math.fmod(x,10))
            x = int(x/10)

            if (n > MAX//10) or (n == MAX//10 and p >=MAX%10):
                return 0
            if (n<MIN//10) or (n == MIN//10 and p <= MIN%10):
                return 0
            n = n*10 + p

        return n
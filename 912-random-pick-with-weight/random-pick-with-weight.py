class Solution:

    def __init__(self, w: List[int]):
        self.cumsum = [0]*len(w)
        su = 0
        for i in range(len(w)):
            su += w[i]
            self.cumsum[i] = su
        self.s = su

    def pickIndex(self) -> int:
        ran = random.randint(0,self.s-1)
        l = 0
        r = len(self.cumsum)-1
        while l<r:
            mid = (l+r)//2
            if self.cumsum[mid] <= ran:
                l = mid + 1
            else:
                r-=1
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class SeatManager:
    def __init__(self, n: int):
        self.n = n
        self.m = 1
        self.seats = []

    def reserve(self) -> int:
        if self.seats:
            return heapq.heappop(self.seats)
        else:
            r = self.m
            self.m += 1
            return r

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
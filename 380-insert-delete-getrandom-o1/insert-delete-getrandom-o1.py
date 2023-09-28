class RandomizedSet:
    def __init__(self):
        self.mp = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.mp:  # Changed the condition
            self.mp[val] = len(self.arr)
            self.arr.append(val)
            return True  # Return True if the item was inserted
        return False

    def remove(self, val: int) -> bool:
        if val in self.mp:
            ind = self.mp[val]
            last = self.arr[-1]
            # Update the map before modifying the array
            self.mp[last] = ind
            # Swap
            self.arr[ind] = last
            self.arr.pop()
            del self.mp[val]
            return True  # Return True if the item was removed
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
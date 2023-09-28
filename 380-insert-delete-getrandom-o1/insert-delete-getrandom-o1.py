class RandomizedSet:

    def __init__(self):
        self.randomset = set()

    def insert(self, val: int) -> bool:
        if val in self.randomset:
            return False
        self.randomset.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomset:
            self.randomset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        ran = random.randint(0, len(self.randomset)-1)
        return list(self.randomset)[ran]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
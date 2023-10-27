# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        self.res = []
        self.curind = 0

        def flatten(nl):
            for it in nl:
                if it.isInteger():
                    self.res.append(it.getInteger())
                else:
                    flatten(it.getList())

        flatten(self.list)
    
    def next(self) -> int:
        if self.curind < len(self.res):
            n = self.res[self.curind]
            self.curind += 1
            return n
    
    def hasNext(self) -> bool:
        return self.curind < len(self.res)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
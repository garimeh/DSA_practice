class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:

        def binarys(row):
            l, h = 0, n-1
            while l <= h:
                mid = (l+h)//2
                if row[mid] == t:
                    return True
                elif t > row[mid]:
                    l = mid+1
                else:
                    h = mid - 1
            return False

        m = len(a)
        n = len(a[0])
        for i in range(m):
            if a[i][0] <= t <= a[i][n-1]:
                return binarys(a[i])
        return False
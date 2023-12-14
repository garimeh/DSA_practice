class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:
        m = len(a)
        n = len(a[0])
        l, h = 0, m*n - 1
        while l <= h:
            mid = (l+h)//2
            row = mid//n
            col = mid%n
            if a[row][col] == t:
                return True
            elif t > a[row][col]:
                l = mid + 1
            else:
                h = mid - 1
        return False
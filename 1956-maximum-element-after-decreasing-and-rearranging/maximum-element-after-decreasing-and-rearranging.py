class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        n = len(arr)
        for i in range(n):
            arr[i] = min(prev+1, arr[i])
            prev = arr[i]

        return arr[n-1]
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def largest_subsequence(arr, k):
            drop = len(arr) - k
            stack = []
            for num in arr:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge_max(arr1, arr2):
            ans = []
            while arr1 and arr2:
                if arr1 > arr2:
                    ans.append(arr1.pop(0))
                else:
                    ans.append(arr2.pop(0))
            ans.extend(arr1 or arr2)
            return ans

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            large1 = largest_subsequence(nums1, i)
            large2 = largest_subsequence(nums2, k - i)
            ans = merge_max(large1.copy(), large2.copy())
            best = max(best, ans) if best else ans
        return best

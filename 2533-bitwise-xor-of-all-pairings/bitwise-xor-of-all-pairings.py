class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n, m = len(nums1), len(nums2)
        freq = {}
        for num in nums1:
            if m%2:
                ans ^= num
        for num in nums2:
            if n%2:
                ans ^= num

        return ans
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        xor1, xor2 = 0,0

        if n%2:
            for num in nums2:
                xor2^=num

        if m%2:
            for num in nums1:
                xor1^=num
        return xor2^xor1
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n, m = len(nums1), len(nums2)
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num,0) + m
        for num in nums2:
            freq[num] = freq.get(num,0) + n
        for num in freq: 
            if freq[num]%2:
                ans ^= num
        return ans
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1
        # Find the rightmost element which is smaller than its next element
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                pivot = i
        
        if pivot == -1:
            nums.reverse()
            return
        
        # Find the rightmost element which is greater than nums[pivot] from the right side
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                # Swap the pivot and the found element
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
        
        # Reverse the subarray to the right of the pivot to get the next permutation
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

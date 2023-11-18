class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(low, mid, high):
            temp = []
            l, r = low, mid+1

            while (l <= mid and r <= high):
                if nums[l] <= nums[r]:
                    temp.append(nums[l])
                    l += 1
                else:
                    temp.append(nums[r])
                    r += 1
            while l <= mid:
                temp.append(nums[l])
                l += 1
            
            while r <= high:
                temp.append(nums[r])
                r += 1

            for i in range(low, high+1):
                nums[i] = temp[i - low]
                
        def mergesort(nums, low, high):
            if low >= high: return
            mid = (low+high)//2
            mergesort(nums, low, mid)
            mergesort(nums, mid+1, high)
            merge(low, mid, high)
        
        mergesort(nums, 0, len(nums) - 1)
        return nums
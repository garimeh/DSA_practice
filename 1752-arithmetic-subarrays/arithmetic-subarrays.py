class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            left, right = l[i], r[i]
            subarray = sorted(nums[left:right+1])

            if len(subarray) < 2:
                ans.append(False)
                continue

            cd = subarray[1] - subarray[0]
            arithmetic = True
            for j in range(1, len(subarray)):
                if subarray[j] - subarray[j - 1] != cd:
                    arithmetic = False
                    break
            ans.append(arithmetic)

        return ans
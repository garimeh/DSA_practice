class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if maxans:
                    maxans = max(num[i:i+3], maxans)
                else:
                    maxans = num[i:i+3]
        return maxans

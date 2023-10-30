class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])  

        cur = intervals[0]
        ans = []

        for i in range(1, len(intervals)):
            st, en = intervals[i]

            if st <= cur[1]:
                cur[1] = max(cur[1], en)
            else:
                ans.append(cur)
                cur = [st, en]

        ans.append(cur) 
        return ans
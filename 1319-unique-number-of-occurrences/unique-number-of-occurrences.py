class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrMap = {}
        for i,e in enumerate(arr):
            if e in arrMap:
                arrMap[e] = arrMap[e] + 1
            else:
                arrMap[e] = 1
        all_values = list(arrMap.values())
        s_values = set(all_values)
        if len(all_values) == len(s_values):
            return True
        else:
            return False
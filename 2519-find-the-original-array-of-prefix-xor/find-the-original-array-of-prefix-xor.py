class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [0]*len(pref)
        ans[0] = pref[0]
        cur = pref[0]
        for i in range(1, len(pref)):
            ans[i] = pref[i]^pref[i-1]
        return ans
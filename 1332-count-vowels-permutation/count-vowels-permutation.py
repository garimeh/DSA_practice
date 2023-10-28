class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prev = [1,1,1,1,1]

        a, e, i, o, u = 0,1,2,3,4
        mod = 10**9 + 7

        for j in range(2,n+1):
            cur = [0,0,0,0,0]
            cur[a] = (prev[e] + prev[i] + prev[u])%mod
            cur[e] = (prev[a] + prev[i])%mod
            cur[i] = (prev[e] + prev[o])%mod
            cur[o] = (prev[i])%mod
            cur[u] = (prev[i] + prev[o])%mod
            prev = cur
            
        return sum(prev)%mod
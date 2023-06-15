    def minWindow(self, s: str, t: str) -> str:

        counter = collections.Counter(t)
        missing = len(t)
        left, right = 0, 0
        res = ""
        reslen = float('inf')
        
        while right<len(s):

            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]]>=0:
                    missing -= 1
                

            while missing==0:
                if right-left+1<reslen:
                    reslen = right-left+1
                    res = s[left:right+1]

                if s[left] in counter:
                    counter[s[left]] += 1
                    if counter[s[left]]>0:
                        missing += 1
                        
                left += 1
                
            right += 1
            
        return res
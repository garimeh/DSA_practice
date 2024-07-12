class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = list(s)
        def helper(inp, tar, ppr):
            tp, write = 0, 0
            for read in range(len(inp)):
                inp[write] = inp[read]
                write += 1

                if write > 1 and inp[write - 2] == tar[0] and inp[write - 1] == tar[1]:
                    write -= 2
                    tp += ppr
            del inp[write:]
            return tp

        res = 0
        if x > y:
            top = "ab"
            tscore = x
            bot = "ba"
            bscore = y
        else :
            top = "ba"
            tscore = y
            bot = "ab"
            bscore = x
        res += helper(s, top, tscore)
        res += helper(s, bot, bscore)
        return res
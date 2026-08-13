class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i] if len(s) > len(t) else t[i]
        return s[-1] if len(s) > len(t) else t[-1]
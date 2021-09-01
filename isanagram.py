class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
            return True

S = Solution()
s = "anargram"
t = "naargram"
print(S.isAnagram(s, t))
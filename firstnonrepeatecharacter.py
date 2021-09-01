class Solution:
    def firstUniqChar(self,s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return s.index(s[i])
        return -1
S=Solution()
x="pleeleeeueetty"
print(S.firstUniqChar(x))
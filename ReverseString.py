class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s=s[::-1]
        return s


S = Solution()
X = ["h","e","l","l","o"]
print(S.reverseString(X))
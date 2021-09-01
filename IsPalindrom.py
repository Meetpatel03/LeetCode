class Solution:
    def isPalindrome(self, s):
        s=list(s.lower())
        l=[]
        for i in s:
            if i.isalnum() == True:
                l.append(i)
        return l == l[::-1]


s=Solution()
m="A man,   plan, a canal: Panama"
print(s.isPalindrome(m))
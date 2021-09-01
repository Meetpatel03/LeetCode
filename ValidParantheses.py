class Solution:
    start_list = ["(", "[", "{"]
    end_list = [")", "[", "}"]

    def isValid(self, s):
        start_list = ["(", "[", "{"]
        end_list = [")", "]", "}"]
        stack = []
        for i in s:
            if i in start_list:
                stack.append(i)
            elif i in end_list:
                position = end_list.index(i)
                if ((len(stack) > 0) and (start_list[position] == stack[len(stack) - 1])):
                    stack.pop()
                # if len(stack)==0 or start_list[position]!=stack.pop():
                else:
                    return False
        return len(stack) == 0


s = Solution()
string = "()[]{}"
print(s.isValid(string))





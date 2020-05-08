"""
s = "3[a]2[bc]", return "aaabcbc"
s = "3[a2[c]]", return "accaccacc"
s = "2[abc]3[cd]ef", return "abcabccdcdcdef"
Time/Space complexity = O(N)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        
        if not s:
            return s
        
        stack = []
        temp = []
        temp_int = []
        braces = True
        for i in s:
            # check for string 
            if i == ']':
                # check for string
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())

                #pop closing braces
                stack.pop()
                # check for number
                while stack and stack[-1].isdigit():
                    temp_int.append(stack.pop())

                no = int(''.join(temp_int[::-1]))
                temp_string = ''.join(temp[::-1])
                stack.append(temp_string*int(no))
                temp = []
                temp_int =[]
    
            else:
                stack.append(i)
    
        return ''.join(stack)
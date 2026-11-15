class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_modified = []
        t_modified = []

        # while i <= (len s) - 1:
        #     for i in range(len s):
        #         if s[i + 1] != "#":
        #             s_modified.append(s[i])
        
        # while i + 1 <= (len t):
        #     for i in range(len t):
        #         if t[i + 1] != "#":
        #             t_modified.append(t[i])

        # return t_modified == s_modified
        
        s_stack = []
        for char in s:
            
            if char != "#":
                s_stack.append(char)

            elif not s_stack:
                pass
            else:
                s_stack.pop()

        t_stack = []
        for char in t:
            if char != "#":
                t_stack.append(char)
            elif not t_stack:
                pass
            else:
                t_stack.pop()

        return s_stack == t_stack
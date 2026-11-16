class Solution:
    def removeDuplicates(self, s: str) -> str:
        # chars = list(s)
        # i = 0  # where to place the next valid char
        
        # for j in range(len(s)):
        #     chars[i] = chars[j]
            
        #     # if the current char is the same as the one before, step back
        #     if i > 0 and chars[i] == chars[i - 1]:
        #         i -= 1
        #     else:
        #         i += 1
                
        # return "".join(chars[:i])

        stack = []
        # stack keeps track of all elements, if the element is already
        # in the stack (specifically the latest element, then
        # remove it, otherwise add the element)
        for char in s:
            # If the current char matches the top of the stack, remove both
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
                
        return "".join(stack)
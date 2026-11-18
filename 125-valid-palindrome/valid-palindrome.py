class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        
        stack = []
        mid = len(cleaned) // 2
        
        # add the first half of the strng to the stack
        for i in range(mid):
            stack.append(cleaned[i])
            
        # determine where the second half starts
        # if the string length is odd, skip the exact middle character
        if len(cleaned) % 2 == 0:
            start_second_half = mid
        else:
            start_second_half = mid + 1
            
        # compare
        for i in range(start_second_half, len(cleaned)):
            if stack.pop() != cleaned[i]: # pops the last element
                return False
                
        return True
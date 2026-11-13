class Solution:
    def addDigits(self, num: int) -> int:
        
        if num >= 10:
            while num >= 10:
                total = 0 # reset the total 
                for digit in str(num):
                    total += int(digit)
                    num = total # new number is the total
        else:
            return num
            
        return total

            
            
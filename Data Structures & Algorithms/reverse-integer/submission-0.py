class Solution:
    def reverse(self, x: int) -> int:
        orig = x
        x = abs(x)
        rev = 0
        while(x>0):
            dig = x%10
            rev = rev*10 + dig
            x = x//10
            
        if orig < 0:
            rev = -rev
            
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
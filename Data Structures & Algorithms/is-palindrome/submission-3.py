class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while(low <= high):
            while(low <= high  and not s[low].isalnum()):
                low = low +1
            while(high >= low  and not s[high].isalnum()):
                high = high - 1    
            if(low <= high and s[low].isalnum() and s[high].isalnum() and s[low].lower() != s[high].lower()):
                return False
            else:    
                low += 1
                high -=1
        return True    
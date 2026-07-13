class Solution:
    def isPalindrome(self,s:str,low:int,high:int) -> bool:
        while(low <= high):
            if s[low] != s[high]:
                return False
            low +=1
            high -=1
        return True        

    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) -1
        while(low <= high):
            if (s[low] != s[high]):
               res = self.isPalindrome(s,low,high-1) or self.isPalindrome(s,low + 1,high)
               return res
            else:
                low = low + 1
                high = high -1
        return True                                    
        
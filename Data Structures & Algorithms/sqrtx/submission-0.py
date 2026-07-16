class Solution:
    def square(self,x:int) -> int:
        return x*x
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = x
        while(low <= high):
            mid = int((low + high) / 2)
            if self.square(mid) <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid -1
        return ans            


class Solution:
    def num_of_hours(self,piles: List[int],k:int) -> int:
        counter = 0
        for i in range(len(piles)):
            if piles[i] % k == 0:
                counter += piles[i] // k
            else:
                counter = counter + (piles[i]//k) + 1
        return counter            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = piles[0]
        for i  in range(len(piles)):
            high = max(piles[i],high)
        ans = high
        while(low <= high):
            mid = (low + high)//2
            if self.num_of_hours(piles,mid) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans               
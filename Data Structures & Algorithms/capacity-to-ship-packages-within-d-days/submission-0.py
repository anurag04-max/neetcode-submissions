class Solution:
    def num_of_days(self,w:List[int],c:int) -> int:
        d = 1
        s = 0
        for i in range(len(w)):
            if s + w[i] <= c:
                s = s + w[i]
            else:
                d+=1
                s = w[i]
        return d         

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)
        ans = l
        while l <= h:
            mid = (l + h) //2
            if self.num_of_days(weights,mid) <= days:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans            
        
class Solution:
    def combinations(self,i,n,k,ans,subset):
        if k == 0:
            ans.append(subset.copy())
            return
        if k < 0 or i > n:
            return
        subset.append(i)
        self.combinations(i+1,n,k-1,ans,subset)
        subset.pop()
        self.combinations(i + 1,n,k,ans,subset)           
    def combine(self, n: int, k: int) -> List[List[int]]:
        i = 1
        subset = []
        ans = []
        self.combinations(i,n,k,ans,subset)
        return ans
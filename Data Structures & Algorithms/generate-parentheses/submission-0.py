class Solution:
    def paranthesis(self,st,en,n,subset,ans):
        if st + en == 2*n:
            ans.append(subset)
            return
        if st < n:
            subset+='('
            self.paranthesis(st + 1,en,n,subset,ans)
            subset = subset[:-1]
        if en < st:
            subset+=')'
            self.paranthesis(st,en + 1,n,subset,ans)
            subset = subset[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        st = 0
        en = 0
        subset = ""
        ans = []
        self.paranthesis(st,en,n,subset,ans)
        return ans
        
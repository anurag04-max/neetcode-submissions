class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 1:
            return strs[0]
        i = 0 
        j = 0
        while i < len(strs[0]) and j < len(strs[1]):
            if strs[0][i] == strs[1][j]:
                ans += strs[0][i]
                i+=1
                j+=1
            else:
                break
        k = 2
        new_ans=""
        while(k < len(strs)):
            i = 0
            for ch in strs[k]:
                if i < len(ans) and ans[i] == ch:
                    new_ans += ch
                    i+=1
                else:
                    break
            ans = new_ans
            new_ans = ""
            k+=1
        return ans                
                            
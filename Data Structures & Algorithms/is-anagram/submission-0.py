class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_mp = {}
        for i in range(len(s)):
            hash_mp[s[i]] = hash_mp.get(s[i],0) + 1
        for i in range(len(t)):
            if t[i] not in hash_mp:
                return False
            hash_mp[t[i]] = hash_mp[t[i]] - 1
            if hash_mp[t[i]] == 0:
                del hash_mp[t[i]] 
        if len(hash_mp) > 0:
            return False
        return True               
        
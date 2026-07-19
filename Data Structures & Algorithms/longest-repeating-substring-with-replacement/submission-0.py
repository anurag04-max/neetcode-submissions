class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_sum = 0
        max_freq = 0
        maxl = 0
        l = 0
        r = 0
        freq_map = {}
        while(r < len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq,freq_map[s[r]])
            freq_sum += 1
            while(freq_sum - max_freq > k):
                freq_map[s[l]]-=1
                freq_sum -=1
                if freq_map[s[l]] == 0:
                    del  freq_map[s[l]]
                l+=1
                max_key = max(freq_map,key = freq_map.get)
                max_freq = freq_map[max_key]
            if freq_sum - max_freq <=k:
                maxl = max(maxl,r-l + 1)
                r +=1
        return maxl                


        
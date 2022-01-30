class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        substring = ''
        
        for char in s:
            if char not in substring:
                substring +=char
                ans = max(ans, len(substring))
            else: #repeat!!
                repeatIndex = substring.index(char) #now we know where to cut it off
                substring = substring[repeatIndex + 1:]
                
                #add the char to the end of new substring
                substring +=char
                                
        
        return ans
        
        
        
        
        
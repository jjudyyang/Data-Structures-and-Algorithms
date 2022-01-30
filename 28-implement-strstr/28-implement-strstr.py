class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #loop through the list
        if not needle:
            return 0
        
        return haystack.find(needle)
        
        
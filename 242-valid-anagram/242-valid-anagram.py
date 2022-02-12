class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #store everything in hashmap 
        
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        
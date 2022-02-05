class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #get rid of the possible strings after
        index = len(s) - 1 #working backwards
        
        while index >= 0 and s[index] == " ":
            index-=1
            
        # find the length of the last word
        output = 0
        while index >=0 and s[index] != " ":
            index-=1 #decrease the index
            output+=1 #increase the length
        
        return output
    
            
        
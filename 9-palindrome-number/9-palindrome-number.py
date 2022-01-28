class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x < 0):
            return False
        

        #convert to string
        palindrome = str(x)
        
        
        if len(palindrome) == 2:
            if(palindrome[0] != palindrome[1]):
                return False
            
        
        left = 0 
        right = len(palindrome) - 1
        
        while(left < right):
            if(palindrome[left] != palindrome[right]):
                return False
            else:
                left +=1
                right -=1
                
        return True
        
class Solution:
    def reverse(self, x: int) -> int:
        
        MAX = 2147483647    #2^31 -1
        MIN = 2147483648 * -1
        
        output = 0
        #assuming we cannot convert it into a string
        
        #1 figure out how many digits it is 
        temp = abs(x)
        digits = 0
        while temp > 0:
            temp = temp//10
            digits +=1
        
        negative = 0
        #2 start chopping away from the end
        if x < 0:
            negative = 1
            x = x*(-1)
        
        while digits > 0:
                num = x % 10
                output += num * pow(10, digits-1)
                x = x //10
                digits -=1

        if negative == 1:
            output = output * -1
            
        if output > MAX or output < MIN:
            return 0
            
        return output

        
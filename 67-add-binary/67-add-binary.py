class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        # convert a and b into integers 
        # add them together
        #convert to binary
        
        aa = int(a, 2)
        bb = int(b, 2)
        
        
        return "{0:b}".format(aa+bb)
        
        
        
        
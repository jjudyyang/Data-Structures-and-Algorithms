class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        #keys: values 
        #list numbers : index of number
        
        length = len(nums)
        
        for index in range(length):
            search = target - nums[index]
            if search in dictionary:
                # yay we found it 
                return [index, dictionary[search]]
            #if not in the dictonary, add it to the dictionary 
            dictionary[nums[index]] = index
            
        
    
        
        
            
        
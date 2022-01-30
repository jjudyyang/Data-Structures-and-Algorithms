class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        #dictionaries are key value pairs
        #return indexes of numbers, not the actual numbers
        
        for index in range(len(nums)):
            #check if number exists in dictionary
            search = target - nums[index]
            
            if search in dictionary:
                #yay! we found the pairs 
                return [index, dictionary.get(search)]
            
            #if search is not in the dictionary, we store it into the dictionary
            dictionary[nums[index]] = index
            
                
            
        
    
        
        
            
        
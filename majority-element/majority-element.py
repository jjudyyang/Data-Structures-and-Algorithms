class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        
        #key : value , number : how many times it appears
        
        for index in range(len(nums)):
            if nums[index] not in dictionary: #add the number to dictionary as key
                dictionary[nums[index]] = 1
                
            dictionary[nums[index]] += 1
            
        #find largest value in dictionary
        Keymax = max(zip(dictionary.values(), dictionary.keys()))[1]
        return Keymax
                
            
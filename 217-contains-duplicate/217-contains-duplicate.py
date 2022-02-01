class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for num in nums:
            if num not in dictionary:
                dictionary[num] = None
            
            else:
                return True
        return False
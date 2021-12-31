class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {
             
        } # mapping value : index
        
        i = 0;
        while(i < len(nums)):
            difference = target - nums[i]
            if difference in hashMap:
                return[hashMap[difference], i]
            
            hashMap[nums[i]] = i # add to hashmap if does not exist 
            i+=1
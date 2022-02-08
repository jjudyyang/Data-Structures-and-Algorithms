class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        
        #find index of target
        
        for x in range(len(nums)):
            if nums[x] == target:
                return x
        
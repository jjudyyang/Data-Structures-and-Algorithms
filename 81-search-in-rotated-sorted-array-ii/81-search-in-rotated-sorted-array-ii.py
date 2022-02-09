class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        for x in range(len(nums)):
            if nums[x] == target:
                return True
        
        return False
        
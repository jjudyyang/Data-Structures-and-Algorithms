class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        tempList = [0] * n
        
        for x in range(n):
            tempList[ nums[x] - 1] +=1
            
        output = []
        for y in range(n):
            if tempList[y] == 0:
                output.append(y + 1)
                
        return output
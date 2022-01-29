class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        #element in the middle is only counted once
        row = 0
        col = 0
        size = len(mat)
        
        output = 0
        
        for x in range(size):
            output += mat[row][col]
            row +=1
            col +=1
        
        row = 0
        col = size - 1 
        
        for y in range(size):
            output += mat[row][col]
            col -= 1
            row += 1
            
        if size % 2 == 1:
            duplicate = size//2
            output -= mat[duplicate][duplicate]
                
        return output
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
stack = [1,2,4]
root = 
result = [4]


"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if root is None:
            return []
        
        stack = []
        result = []

        while root is not None or stack != []:
            
            while root is not None:
                stack.append(root)
                root = root.left
                
            temp = stack[-1].right
            if temp is not None:
                root = temp
                
            else:
                temp = stack.pop()
                result.append(temp.val)
                while stack != [] and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
                    
        return result 
            
                
        
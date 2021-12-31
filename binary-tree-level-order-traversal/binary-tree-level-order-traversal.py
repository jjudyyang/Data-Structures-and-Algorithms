# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        levels = []
        
        def helper(node, level):
            
            if len(levels) == level:
                levels.append([]) #add empty list thing to list
                
            #append the current node value to the list in the list
            levels[level].append(node.val)
            
            #for the next level
            if node.left:
                helper(node.left, level +1)
            if node.right:
                helper(node.right, level +1)
                
        
        #call the helper function  starting at the root and level 0
        helper(root,0)
                
        return levels
            
        
        
        
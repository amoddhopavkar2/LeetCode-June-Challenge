# PROBLEM STATEMENT - Invert a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        else:
            temp = root
            
            Solution.invertTree(self, root.left)
            Solution.invertTree(self, root.right)
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            return root
# PROBLEM STATEMENT - Search in a Binary Search Tree
# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

class Solution(object):
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current_node = root
        while current_node:
            if current_node.val == val:
                return current_node
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, root):
        if not root:
            return 0
        else:
            return max(self.height(root.left),self.height(root.right))+1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        else:
            left_h = self.height(root.left)
            right_h = self.height(root.right)
            if abs(left_h-right_h) >1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
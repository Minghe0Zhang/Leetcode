"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up 
all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right: # leaf node
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)



        # iteration
        if not root:
            return False
        stack = [(root,sum)]
        while stack:
            cur_node, cur_sum = stack.pop()
            # print(cur_sum)
            val  = cur_node.val
            if not cur_node.left and not cur_node.right and cur_sum-val==0:
                return True
            if cur_node.left:
                stack.append((cur_node.left, cur_sum-val))
            if cur_node.right:
                stack.append((cur_node.right, cur_sum-val))
        
        return False



    
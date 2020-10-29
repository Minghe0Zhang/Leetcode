# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if root is None:
        #   return None
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
          return root
        elif p.val <= root.val and q.val<=root.val:
          return self.lowestCommonAncestor(root.left, p, q)
        else:
          return self.lowestCommonAncestor(root.right, p, q)


        # iterative method
        queue = [root]
        while(queue):
          cur_node = queue.pop(0)
          if (p.val <= cur_node.val and q.val >= cur_node.val) or (p.val >= cur_node.val and q.val <= cur_node.val):
            return cur_node
          elif p.val <= cur_node.val and q.val<=cur_node.val:
            queue.append(cur_node.left)
          else:
            queue.append(cur_node.right)
            


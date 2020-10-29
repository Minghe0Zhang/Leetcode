"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        cur_head = head
        while cur_head:
            label = cur_head.label
            new_node = RandomListNode(label)
            new_node.next = cur_head.next
            cur_head.next = new_node
            cur_head = new_node.next

        cur_head = head
        while cur_head:
            new_node = cur_head.next
            if cur_head.random:
                new_node.random = cur_head.random.next
            cur_head = new_node.next

        cur_head = head
        new_head = head.next
        while cur_head is not None and cur_head.next:
            next_node = cur_head.next
            cur_head.next = next_node.next
            cur_head = next_node

        return new_head
        
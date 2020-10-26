"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = ListNode(0)
        larger  = ListNode(0)
        cur_s   = smaller
        cur_l   = larger
        while head:
            if head.val >= x:
                cur_l.next = ListNode(head.val)
                cur_l      = cur_l.next
            else:
                cur_s.next = ListNode(head.val)
                cur_s      = cur_s.next
            head = head.next
        
        cur_s.next = larger.next
        return smaller.next
        
"""
Reverse a singly linked list.


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # cur   = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return cur
        cur = head
        pre = None
        while cur:
            temp     = cur.next
            cur.next = pre
            pre      = cur
            cur      = temp
        return pre
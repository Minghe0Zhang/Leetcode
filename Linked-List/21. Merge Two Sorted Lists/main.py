"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by 
splicing together the nodes of the first two lists.


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        ans_head = ListNode(0)
        cur      = ans_head
        while(l1 is not None and l2 is not None):
            if(l1.val > l2.val):
                cur.next = ListNode(l2.val)
                cur      = cur.next
                l2       = l2.next
            else:
                cur.next = ListNode(l1.val)
                cur      = cur.next
                l1       = l1.next
        
        if l1 is not None:
            cur.next     = l1
        if l2 is not None:
            cur.next     = l2
        return ans_head.next
        


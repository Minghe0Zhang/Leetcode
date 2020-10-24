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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(1)
        cur = ans
        if not head or not head.next:
            return head
        while head and head.next:
            slow, fast = head, head.next
            head       = fast.next
            fast.next  = slow
            slow.next  = head
            cur.next   = fast
            cur        = cur.next.next
            
        return ans.next

        # # recursion
        # if head is None or head.next is None:
        #     return head

        # first_node = head
        # second_node = head.next

        # first_node.next = self.swapPairs(second_node.next)
        # second_node.next = first_node

        # return second_node
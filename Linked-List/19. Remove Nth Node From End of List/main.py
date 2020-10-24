"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ans = head

        fast = low = head
        for j in range(n):
            fast = fast.next
        if fast == None:
            return ans.next
        while(fast.next):
            fast = fast.next
            low  = low.next
        
        
        low.next  = low.next.next
        return ans
        
        


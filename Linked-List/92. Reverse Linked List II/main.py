"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m==n:
            return head
        pre = None
        cur = head
        cnt = 1
        while(cnt < m):
            pre = cur
            cur = cur.next
            cnt += 1
        
        before = pre
        after  = cur
        pre = cur
        cur = cur.next
        
        while(cnt < n):
            temp = cur.next
            cur.next = pre
            pre  = cur
            cur  = temp
            cnt  += 1
        if before == None:
            after.next  = cur
            return pre
        before.next = pre
        after.next  = cur
        return head
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        cnt = 0
        cur = head
        
        while(cnt < k-1):
            cnt+=1
            cur = cur.next
            if not cur:
                return head
        
        tail = head.next
        mid  = head
        # print(tail.val)
        for i in range(k-1):
            temp = tail.next
            tail.next = head
            mid.next  = temp
            head, tail= tail, mid
            tail = tail.next
            
        mid.next = self.reverseKGroup(tail, k)
        return head
        
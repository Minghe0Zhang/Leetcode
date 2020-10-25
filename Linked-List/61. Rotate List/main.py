"""

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         cnt = 1
#         cur = head
#         if head is None or k==0 or head.next is None:
#             return head
#         while cur.next:
#             cnt += 1
#             cur = cur.next
#         # print(cnt)
#         k = k%cnt
#         if k ==0:
#             return head
        
#         fast = slow = head
#         for i in range(k):
#             fast = fast.next
        
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
#         ans = slow.next
#         fast.next = head
#         slow.next = None
#         return ans
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer
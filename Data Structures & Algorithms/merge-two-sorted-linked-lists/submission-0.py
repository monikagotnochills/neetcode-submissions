# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Create a dummy node to act as the start of the merged list
        dummy = ListNode()

        # Tail always points to the last node in the merged list
        tail = dummy

        # Continue until one of the lists becomes empty
        while l1 and l2:

            # If current node of l1 is smaller
            if l1.val < l2.val:
                tail.next = l1      # Attach l1 node
                l1 = l1.next        # Move l1 forward

            else:
                tail.next = l2      # Attach l2 node
                l2 = l2.next        # Move l2 forward

            # Move tail to the newly attached node
            tail = tail.next

        # Attach whichever list is not empty
        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        # Skip the dummy node and return the real head
        return dummy.next
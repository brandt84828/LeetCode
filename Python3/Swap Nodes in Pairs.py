# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy
        keep = None
        while cur and cur.next:
            keep = cur.next.next
            cur.next.next = cur
            prev.next = cur.next
            cur.next = keep

            prev = cur
            cur = cur.next

        return dummy.next
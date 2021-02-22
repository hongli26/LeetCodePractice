# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur:
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
            
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
            
        return dummy.next

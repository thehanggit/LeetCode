# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # dummy = ListNode(0, head)
        # prev = dummy
        

        # for _ in range(left - 1):
        #     prev = prev.next
        
        # reverse_start = prev.next
        # curr = reverse_start

        # next_node = curr.next
        
        # for _ in range(right - left):
        #     temp = next_node.next
        #     next_node.next = curr
        #     curr = next_node
        #     next_node = temp
        
        # prev.next = curr
        # reverse_start.next = next_node
        

        # return dummy.next

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        reverse_start = prev.next
        curr = reverse_start

        next_node = curr.next

        for _ in range(right - left):
            temp = next_node.next
            next_node.next = curr
            curr = next_node
            next_node = temp

        prev.next = curr
        reverse_start.next =  next_node

        return dummy.next
        
        
        
        
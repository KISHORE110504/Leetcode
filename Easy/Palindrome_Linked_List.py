# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev_node = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        while slow is not None: 
            next_temp = slow.next  
            slow.next = prev_node  
            prev_node = slow 
            slow = next_temp  
        
        while prev_node is not None:
            if head.val != prev_node.val:
                return False
            else: 
                head = head.next 
                prev_node = prev_node.next
        return True

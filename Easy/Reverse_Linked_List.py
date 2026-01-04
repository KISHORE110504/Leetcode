'''Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        while curr_node is not None: #looping till the current node is not none
            next_temp = curr_node.next  #next node of the current node is the temporary next node
            curr_node.next = prev_node  #previous node(NONE) is the current node's next node
            prev_node = curr_node  #previous node is the current node
            curr_node = next_temp  #current node is now the temporary next node
        return prev_node  #returning the reversed list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_table = {}

        #   **Solution #1**
        while head:
            if head in nodes_table: return True
            else: nodes_table[head] = head
            head = head.next
        return False
    
        #   **Solution #2**
        s = head
        f = head

        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next
            if s == f: return True
        return False
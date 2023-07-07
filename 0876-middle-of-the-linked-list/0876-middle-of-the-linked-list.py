# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow  = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        """slow_ptr=head
        fast_ptr=head
        while slow_ptr and fast_ptr.next:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        return slow_ptr.val"""
            
        
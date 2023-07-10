# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """if(not head or not head.next or k==0):
            return head
        
        len=1
        temp=head
        while temp.next:
            temp=temp.next
            len+=1
        temp.next=head
        k=k%len
        k=len-k
        
        while(k):
            tem=temp.next
            k-=1
            
        head=temp.next
        temp.next=None
        return head"""
        
        
                     
        if not head or not head.next or k==0:return head 
        curr,size=head,1
        
        while curr.next:
            size+=1
            curr=curr.next
            
        k=k%size
        k=size-k
        curr.next=head
        while k:
            curr=curr.next
            k-=1
            
        head=curr.next
        curr.next=None
        
        return head
        
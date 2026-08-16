# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=head
        a=[]
        while head!=None:
            a.append(head.val)
            head=head.next
       

        head=l
        for i in range(0,len(a),2):
            head.val=a[i]
            head=head.next

        for i in range(1,len(a),2):
            head.val=a[i]
            head=head.next
        head=l
        return head

        
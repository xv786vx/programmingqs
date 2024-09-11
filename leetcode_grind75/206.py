# 206. Reverse Linked List

# My solution (could optimize since extra space is used but wtv)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        q = []
        dummy = head
        while dummy:
            q.append(dummy.val)
            dummy = dummy.next
        
        dummy2 = head
        i = 1
        while dummy2:
            dummy2.val = q[-i]
            dummy2 = dummy2.next
            i = i+1
        
        return head

#redid this q cleaner
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1, dummy2, stack = head, head, []
        while dummy1:
            stack.append(dummy1.val)
            dummy1 = dummy1.next
        
        while stack:
            dummy2.val = stack.pop()
            dummy2 = dummy2.next
        
        return head
    
    
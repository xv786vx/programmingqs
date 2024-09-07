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
    
    
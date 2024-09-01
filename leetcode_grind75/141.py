# 141. Linked List Cycle

#my solution
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        visited = {}
        while head.next and head.next not in visited:
            visited[head] = True
            head = head.next
        if not head.next:
            return False
        else:
            return True
        
#better solution using two pointers (lowkey same stats though)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slowp = head
        fastp = head

        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            if slowp == fastp:
                return True
        return False

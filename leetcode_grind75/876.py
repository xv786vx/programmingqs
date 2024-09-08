# 876. Middle of the Linked List

#my solution (lowk atrocious memory usage)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1, counter, length = head, 0, 0
        while dummy1:
            dummy1 = dummy1.next
            counter = counter + 1
        
        
        length = int(-((-counter/2) // 1))

        while head:
            if counter > (length):
                counter -= 1
                head = head.next
            else:
                return head
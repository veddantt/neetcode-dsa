class Solution(object):
    def reverse(self,head):
        prev = None
        temp = head
        while temp!=None:
            front = temp.next 
            temp.next = prev
            prev = temp 
            temp = front
        return prev
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        prev = None
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            prev = slow
            slow = slow.next 
            fast = fast.next.next
        second = slow.next 
        slow.next = None
        end_head = self.reverse(second)
        slow = head
        while slow and end_head:
            fl = slow.next
            fr = end_head.next
            slow.next = end_head
            end_head.next = fl
            slow = fl
            end_head = fr
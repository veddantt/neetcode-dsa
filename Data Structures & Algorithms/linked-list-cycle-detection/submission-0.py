class Solution(object):
    def hasCycle(self, head):
        s = set()
        current = head

        while current:
            if current in s:
                return True
            s.add(current)
            current = current.next
        
        return False